'use strict';

app

.controller('View1Ctrl', ['$scope', 'todos', '$stateParams', '$state', function($scope, todos, $stateParams, $state) {
  todos.query().$promise.then(function(data) {
        $scope.todos = data;
        console.log(data);
    });

}]);
