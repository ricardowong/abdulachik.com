var abdulBlog = angular.module('abdul-blog', ['ngResource', 'ngRoute', 'textAngular'])
.run(function ($rootScope, $location, $route, AuthService) {

  $rootScope.$on('$routeChangeStart', function (event, next, current) {
    console.log(next);
    try {
      if (next.access.restricted && AuthService.isLoggedIn() === false) {
        $location.path('/login');
        $route.reload();
      }
  } catch (e) {
      if (AuthService.isLoggedIn() === false) {
        $location.path('/login');
        $route.reload();
      }
    };
  });

})
.config(['$routeProvider', function ($routeProvider) {

    $routeProvider
      .when('/', {
        templateUrl: 'static/app/home/home.html', 
        controller: 'HomeController',
        access: {restricted: false}})
      .when('/soon', {
        templateUrl: 'static/app/redirects/soon.html', 
        controller: 'RedirectsController',
        access: {restricted: false}})
      .when('/login', {
        templateUrl: 'static/app/auth/login.html', 
        controller: 'LoginController',
        access: {restricted: false}})
      .when('/logout', {
        controller: 'LogoutController',
        access: {restricted: true}})
      .when('/dashboard', {
        templateUrl : 'static/app/dashboard/dashboard.html',
        controller: 'DashboardController',
        access: {restricted: true}})
      .otherwise({redirectTo: '/'});

  }]);



