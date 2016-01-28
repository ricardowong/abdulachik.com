// Declare app level module which depends on filters, and services

var abdulBlog = angular.module('abdul-blog', ['ngResource', 'ngRoute', 'firebase']);
abdulBlog.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html', 
        controller: 'HomeController'})
      .when('/soon', {
        templateUrl: 'views/redirects/soon.html', 
        controller: 'RedirectsController'})
      .when('/login', {
        templateUrl: 'views/login/login.html', 
        controller: 'LoginController'})
      .otherwise({redirectTo: '/'});

  }]);



