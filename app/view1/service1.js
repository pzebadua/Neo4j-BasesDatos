'use strict';

angular.module('myApp.service1', ['ngRoute'])

.service('RecepieService', function($q,$http) {
    
    return {
        getRecepie: function() {
            //return $http.get("http://localhost:7474/json.py");
            return $http.get("http://ubiquitous.csf.itesm.mx/~pddm-1018302/content/parcial2/examen/Cars/backend/servicio.select.php");
        },
        
        getIngredients: function(idIngredient){
            return $http.get("http://ubiquitous.csf.itesm.mx/~pddm-1018302/content/parcial2/examen/Cars/backend/servicio.select.php");
        },
        
        getTools: function(idTool){
            return $http.get('http://ubiquitous.csf.itesm.mx/~pddm-1018302/content/parcial2/examen/Cars/backend/servicio.insert.php?id=' + idTool);
        }
        
    }
});