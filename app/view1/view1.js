'use strict';

angular.module('myApp.view1', ['ngRoute','myApp.service1'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope','$http','RecepieService',function($scope, $http, RecepieService) {
  /*$scope.recepies = [
    { name: 'Rav4', class: 'info', image: "./img/rav4.jpg", id: 1 },
    { name: 'Impreza', class: 'success',image: "./img/subaru.jpg", id: 2 },
    { name: 'Tsuru', class: 'danger',image: "./img/tsuru.jpg", id: 3 }
  ];*/
    $scope.recepies = [
        {
            id: '',
            ingredients: [{}],
            tools: []
        }
    ]
    
    var plop = {"statements": [{"statement":"MATCH (n:Receta) RETURN n", "parameters":{}}]};
    var ing;

    
        RecepieService.postRecepie(plop).then (
            function(resp){
					//alert("entro");
                $scope.todo = resp.data;
                $scope.recepies = resp.data.results[0].data;
                //console.log($scope.recepies[1].row[0]);
                angular.forEach($scope.recepies, function(recepie, key) {
                    //console.log("receta:" + recepie.name);
ing = {"statements": [{"statement":"match (R:Receta)-[:NECESITA]-(I:Product)where R.id="+recepie.row[0].id+" return I", "parameters":{}}]};
//console.log(ing);
                    RecepieService.postIngredients(ing).then (
                        function(ingr){
                             recepie.ingredients =  ingr.data.results[0].data;
                            console.log(recepie.ingredients);
                        }
                        
                    );
                    
                    RecepieService.getTools(recepie.id).then (
                        function(too){
                             recepie.tools =  too.data;

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