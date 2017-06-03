app.config(["$routeProvider", function ($routeProvider) {
    "use strict";
    $routeProvider.when('/',
        {
            controller: 'homepageController',
            templateUrl: '../app/views/homepage.html',
            resolve: {}
        })
        .otherwise({redirectTo: '/'});
}]);