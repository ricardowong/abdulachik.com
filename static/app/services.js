abdulBlog.factory('AuthService',
  ['$q', '$timeout', '$http', '$rootScope',
  function ($q, $timeout, $http, $rootScope) {

    // create user variable
    $rootScope.user = null;
    function isLoggedIn() {
      if($rootScope.user) {
        return true;
      } else {
        return false;
      }
    }

    function login(email, password) {

      // create a new instance of deferred
      var deferred = $q.defer();

      // send a post request to the server
      $http.post('/login', {email: email, password: password})
        // handle success
        .success(function (data, status) {
          if(status === 200 && data.result){
            $rootScope.user = true;
            deferred.resolve();
          } else {
            $rootScope.user = false;
            deferred.reject();
          }
        })
        // handle error
        .error(function (data) {
          $rootScope.user = false;
          deferred.reject();
        });

      // return promise object
      return deferred.promise;

    }

    function logout() {

      // create a new instance of deferred
      var deferred = $q.defer();

      // send a get request to the server
      $http.get('/logout')
        // handle success
        .success(function (data) {
          $rootScope.user = false;
          deferred.resolve();
        })
        // handle error
        .error(function (data) {
          $rootScope.user = false;
          deferred.reject();
        });

      // return promise object
      return deferred.promise;

    }


    // return available functions for use in controllers
    return ({
      isLoggedIn: isLoggedIn,
      login: login,
      logout: logout
      // ,register: register
    });
}]);