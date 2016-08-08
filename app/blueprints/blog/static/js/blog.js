var blog = angular.module('blog', ['ngRoute', 'ngResource', 'ngSanitize', 'angularTrix', 'ngTagsInput']);

blog.config(['$routeProvider', '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/blog/static/pages/index.html',
        controller: 'BlogIndexCtrl'
      })
      .when('/post/:id', {
        templateUrl: '/blog/static/pages/post.html',
        controller: 'BlogPostCtrl'
      });
}]);

blog.run(function($rootScope, $resource){
    $resource('/api/tag/all').get(function(response){
      $rootScope.tags = response.tags;
    });
})

blog.controller('BlogIndexCtrl', function($scope, $resource){
  $scope.quantity = 4;
  $scope.beginsWith = 4;

  $resource('/api/post/all').get(function(response){
    console.log(response);
    $scope.posts = response.posts;
  });


});
blog.controller('BlogPostCtrl', function($scope, $resource, $routeParams){
  var post_id = $routeParams.id;
  $resource('/api/post/' + post_id).get(function(response){
    $scope.post = response;
  })

});
