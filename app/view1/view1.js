'use strict';

angular.module('myApp.view1', ['ngRoute','myApp.service1'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope','$http','RecepieService',function($scope, $http, RecepieService) {

    var ings = {"statements": [{"statement":"MATCH (n:Product) RETURN n", "parameters":{}}]};
    var ingst = {"statements": [{"statement":"MATCH (n:Product)-[r:ESTA{estado:'vencido'}]->(d:Fechas) RETURN n,d", "parameters":{}}]};


    RecepieService.postAllIngredients(ingst).then (
                        function(ingo){
                             $scope.ingredients =  ingo.data.results[0].data;
                             console.log($scope.ingredients);
                            angular.forEach($scope.ingredients, function(ingp, key) {
                                ingp.row[0].val = false;
                                var countQ = {"statements": [{"statement":"MATCH (n:Product) where n.name = '"+ ingp.row[0].name +"' RETURN count(*)", "parameters":{}}]};
                                RecepieService.postAllIngredients(countQ).then (
                        function(zz){
                            //console.log("ressssss");
                            //console.log(zz.data.results[0].data[0].row[0]);
                            ingp.row[0].size = zz.data.results[0].data[0].row[0];
                        });
                            });
                        }
                        
                    );

	$scope.agregarIngredientes = function(){
		angular.forEach($scope.ingredients, function(ingp, key) {
            console.log(ingp.row[0].val);
            if(ingp.row[0].val)
            {
                            alert("reabastecido");

                    var ingoo = {"statements": [{"statement":"create (P:Product{fecha: 15, fresco: 1, precio: "+ingp.row[0].precio+", peso: "+ingp.row[0].peso+", name: '"+ingp.row[0].name+"',id: "+ingp.row[0].id+"})", "parameters":{}}]};
                    RecepieService.postAllIngredients(ingoo).then (
                        //alert("reabastecido")
                        function(lol){
                            //console.log(lol);
                        }
                        );
            };
         });
	}

    $scope.crear = function(idr){
		 alert(idr);
		 var cre = {"statements": [{"statement":"MATCH (R:Receta)-[r:NECESITA]-(P:Product)-[r2:ESTA]-(F:Fechas) where R.id="+idr+" set r2.estado='vendido' RETURN *", "parameters":{}}]};
		 RecepieService.postCreate(cre).then(
			//alert("vendido"));
         function(resp){
            //console.log(resp.data);
         }
        )
	}
    $scope.recepies = [
        {
            id: '',
            ingredients: [{}],
            tools: []
        }
    ]
    
    var plop = {"statements": [{"statement":"MATCH (n:Receta) RETURN n", "parameters":{}}]};
    var ing;
	 var too;

    
        RecepieService.postRecepie(plop).then (
            function(resp){
					//alert("entro");
                $scope.todo = resp.data;
                $scope.recepies = resp.data.results[0].data;
                //console.log($scope.recepies[1].row[0]);
                angular.forEach($scope.recepies, function(recepie, key) {
                    //console.log("receta:" + recepie.name);
ing = {"statements": [{"statement":"match (R:Receta)-[j:NECESITA]-(I:Product)where R.id="+recepie.row[0].id+" return I", "parameters":{}}]};
var ing2 = {"statements": [{"statement":"MATCH p=(n:Receta)-[r:NECESITA]->(I:Product)where n.id = "+recepie.row[0].id+" RETURN sum(toInt(I.precio)) LIMIT 25", "parameters":{}}]};
too = {"statements": [{"statement":"match (R:Receta)-[:Usa]-(I:Herraminetas)where R.id="+recepie.row[0].id+" return I", "parameters":{}}]};

//console.log(ing);
                    RecepieService.postIngredients(ing).then (
                        function(ingr){
                             recepie.ingredients =  ingr.data.results[0].data;
                             //console.log("sssssss");
                            //console.log(recepie.ingredients);
                        }
                        
                    );
                    RecepieService.postIngredients(ing2).then (
                        function(ingr){
                             recepie.count =  ingr.data.results[0].data[0].row[0];
                             console.log("wedvghcasdbhasdbn");
                             console.log(recepie.count);
                        }
                        
                    );
                    
                    RecepieService.postIngredients(too).then (
                        function(to){
                             recepie.tools =  to.data.results[0].data;

                        }
                        
                    );
                     
                    
                })
            }
        );
    
   
    //var recepies = $scope.recepies;
    /*
    angular.forEach(recepies, function(recepie, key) {
        console.log(recepie.name);
    });*/
    /*
    */
}]);