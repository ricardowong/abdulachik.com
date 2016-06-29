var blog = angular.module('blog',
['ngResource', 'ngRoute', 'ngCookies', 'vcRecaptcha', 'ui.select', 'froala'])
.config(['$routeProvider', function ($routeProvider, $authProvider) {
  // // $authProvider.httpInterceptor = function() { return true; },
  // // $authProvider.withCredentials = true;
  // // $authProvider.tokenRoot = null;
  // $authProvider.baseUrl = '/';
  // $authProvider.loginUrl = '/login';
  // $authProvider.signupUrl = '/admin/signup';
  // // $authProvider.unlinkUrl = '/auth/unlink/';
  // $authProvider.tokenName = 'token';
  // $authProvider.tokenPrefix = 'satellizer';
  // $authProvider.authHeader = 'Authorization';
  // $authProvider.authToken = 'Bearer';
  // $authProvider.storageType = 'localStorage';
    $routeProvider
      .when('/preview', {
        templateUrl: '../static/app/home/home.html',
        controller: 'HomeController',
        access: {restricted: false}})
      .when('/soon', {
        templateUrl: '../static/app/redirects/soon.html',
        controller: 'RedirectsController',
        access: {restricted: false}})
      .when('/logout', {
        controller: 'LogoutController',
        access: {restricted: false}})
      .when('/', {
        templateUrl : '../static/app/dashboard/dashboard2.html',
        controller: 'DashboardController',
        access: {restricted: false}})
      .when('/blog-landing', {
        templateUrl : '../static/app/dashboard/BlogLanding.html',
        controller: 'BlogLandingController',
        access: {restricted: false}})
      .when('/new-post', {
        templateUrl : '../static/app/dashboard/new-post.html',
        controller: 'NewPostController',
        access: {restricted: false}})
      .when('/post/:postid', {
        templateUrl: '../static/app/blog/post.html',
        controller: 'BlogController',
        access: {restricted: false}})
      .when('/contact-me', {
        templateUrl: '/static/app/contact/contact-me.html',
        controller: 'ContactController',
        access: {restricted: false}})
      .otherwise({redirectTo: '/'});

  }])
.run(function ($rootScope, $location, $route, AuthService) {

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

  $rootScope.user = {
    name: "abdul",
    bio: " sup dog",
    startDate: "12-12-1992"
  }
});
