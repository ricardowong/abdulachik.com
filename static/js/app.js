// Declare app level module which depends on filters, and services

var abdulBlog = angular.module('abdul-blog', ['ngResource', 'ngRoute', 'textAngular']);
abdulBlog.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/views/home/home.html', 
        controller: 'HomeController'})
      .when('/soon', {
        templateUrl: 'static/views/redirects/soon.html', 
        controller: 'RedirectsController'})
      .when('/login', {
        templateUrl: 'static/views/login/login.html', 
        controller: 'LoginController'})
      .when('/', {
        templateUrl : 'static/views/dashboard/dashboard.html',
        controller: 'DashboardController'})
      .otherwise({redirectTo: '/'});

  }]);



