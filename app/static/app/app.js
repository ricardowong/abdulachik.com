var blog = angular.module('blog', ['ngResource', 'ngRoute', 'ngCookies', 'textAngular', 'vcRecaptcha', 'ui.select', 'ngSanitize'])
.config(['$routeProvider', function ($routeProvider) {

    $routeProvider
      .when('/', {
        templateUrl: '../static/app/home/home.html', 
        controller: 'HomeController',
        access: {restricted: false}})
      .when('/soon', {
        templateUrl: '../static/app/redirects/soon.html', 
        controller: 'RedirectsController',
        access: {restricted: false}})
      .when('/logout', {
        controller: 'LogoutController',
        access: {restricted: true}})
      .when('/dashboard', {
        templateUrl : '../static/app/dashboard/dashboard.html',
        controller: 'DashboardController',
        access: {restricted: true}})
      .when('/post/:postid', {
        templateUrl: '../static/app/blog/post.html',
        controller: 'BlogController',
        access: {restricted: false}})
      .when('/contact-me', {
        templateUrl: '/static/app/contact/contact-me.html',
        controller: 'ContactController',
        access: {restricted: false}})
      .otherwise({redirectTo: '/'});

  }]).run(function ($rootScope, $location, $route, AuthService) {

  $rootScope.$on('$routeChangeStart', function (event, next, current) {
    try {
      if (next.access.restricted && AuthService.isLoggedIn() === false) {
        $location.path('/');
        $route.reload();
      }
  } catch (e) {
      if (AuthService.isLoggedIn() === false) {
        $location.path('/');
        $route.reload();
      }
    };
  });

});



