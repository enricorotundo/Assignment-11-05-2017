'use strict';

app

.controller('View3Ctrl', ['$scope', 'todos', '$stateParams', '$state', function($scope, todos, $stateParams, $state) {
    var entry = {
        owner: 1,
        status: "active",
        "due_date": null,
        "description": null
    };

    $scope.todo = entry;

    $scope.createTODO = function () {
        console.log($scope.todo);

        var new_todo = new todos($scope.todo);

        new_todo.$save(function (res) {
            $state.go('view1', {}, {reload: true});
        });

    };
}]);
