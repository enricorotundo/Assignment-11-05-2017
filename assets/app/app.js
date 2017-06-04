'use strict';


// Declare app level module which depends on views, and components
var app = angular.module('myApp', [
    'ngResource',
    'ui.router'
])
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider
        .state({
            name: 'view1',
            url: '/todos/',
            templateUrl: 'view1/view1.html',
            controller: 'View1Ctrl'
        }).state({
            name: 'view2',
            url: '/todos/?id',
            templateUrl: 'view2/view2.html',
            controller: 'View2Ctrl'
        });

  $urlRouterProvider.otherwise('/todos/');
}])
.factory('todos', function($resource) {
        return $resource(
            'http://localhost:8000/todos/:id/',
            {},
            {
                'query': {
                    method: 'GET',
                    isArray: false,
                    headers: {
                        'Content-Type':'application/json'
                    }
                },
                'update': {
                    method: 'PUT',
                    headers: {
                        'Content-Type':'application/json'
                    }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });
