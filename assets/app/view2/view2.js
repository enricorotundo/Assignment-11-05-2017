'use strict';

app

.controller('View2Ctrl', ['$scope', 'todos', '$stateParams', '$state', function($scope, todos, $stateParams, $state) {

    var id = $stateParams.id

  var todo = todos.get({ id: id }, function(data) {
    $scope.todo = data;
  });

    $scope.submitTODO = function () {

               console.log(todo);

        todos.update({ id: id }, todo)

    };

}]);
