'use strict';

app

.controller('View2Ctrl', ['$scope', 'todos', '$stateParams', '$state', function($scope, todos, $stateParams, $state) {

    console.log($state.params);
    console.log($stateParams);

    var id = $stateParams.id;

      var todo = todos.get({ id: id }, function(data) {
        $scope.todo = data;
      });

    $scope.submitTODO = function () {
        console.log(todo);
        todos.update({ id: id }, todo).then(function () {
            alert("done");
        })

    };

    $scope.deleteTODO = function () {
        console.log(todo);
        todos.delete({ id: id },
            function (successResult) {
                $state.go('view1', {}, {reload: true});
        }, function (errorResult) {

            });
    };

}]);
