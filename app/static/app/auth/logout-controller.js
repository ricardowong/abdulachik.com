blog.controller('LogoutController',
  ['$scope', '$location', 'AuthService',
  function ($scope, $location, AuthService, $auth) {

    $scope.logout = function () {

      // call logout from service
      AuthService.logout()
        .then(function () {
          $location.path('/login');
        });

    };

}]);
