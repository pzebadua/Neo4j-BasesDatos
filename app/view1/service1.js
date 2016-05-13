'use strict';

angular.module('myApp.service1', ['ngRoute'])

.service('RecepieService', function($q,$http) {

    var baseurl = "http://neo4j:1234@localhost:7474/db/data/transaction/commit";
    
    return {
        getRecepie: function() {
            //return $http.get("http://localhost:7474/json.py");
            return $http.get("http://localhost:8087/1");
        },
        
        getIngredients: function(idIngredient){
            return $http.get("http://ubiquitous.csf.itesm.mx/~pddm-1018302/content/parcial2/examen/Cars/backend/servicio.select.php");
        },
        
        getTools: function(idTool){
            return $http.get('http://ubiquitous.csf.itesm.mx/~pddm-1018302/content/parcial2/examen/Cars/backend/servicio.insert.php?id=' + idTool);
        },
			
        postRecepie: function(query){
            return $http.post(baseurl, query,{
				    headers: {
						'Accepts': 'application/json; charset=UTF-8;'
					}
            });
        },
        
        postIngredients: function(query){
            return $http.post(baseurl, query,{
				    headers: {
						'Accepts': 'application/json; charset=UTF-8;'
					}
            });
        },
        
        postTools: function(query){
            return $http.post(baseurl, query,{
				    headers: {
						'Accepts': 'application/json; charset=UTF-8;'
					}
            });
        },
        postAllIngredients: function(query){
            return $http.post(baseurl,query,{
                headers: {
                    'Accepts': 'application/json; charset=UTF-8;'
                }
            })
        },
			
		  postCreate: function(query){
            return $http.post(baseurl, query,{
				    headers: {
						'Accepts': 'application/json; charset=UTF-8;'
					}
            });
        }
        
    }
});