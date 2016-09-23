Class(UI, 'Sidebar').inherits(Widget)({
  HTML: `<div>
      <ul class="sidebar-nav">
        <li class="sidebar-brand">
          <a href="/">admin</a>
        </li>
      </ul>
      </div
  `,
  ELEMENT_CLASS: 'sidebar-wrapper',
  prototype: {
    menuListElement: null,
    menuOptions: [],
    init: function(config){
      Widget.prototype.init.call(this, config);
      this.element.attr('id', 'sidebar_wrapper');
      this.menuListElement = this.element.find('> .sidebar-nav')
      this.menuOptions.push(new UI.MenuOption({ name : 'create_post', route: '/dashboard/create_post' }));
      this.menuOptions.push(new UI.MenuOption({ name : 'second-option', route: '/dashboard'}));
      this.menuOptions[0].render(this.menuListElement);
      this.menuOptions[1].render(this.menuListElement);
    }
  }
});

Class(UI, 'MenuOption').inherits(Widget)({
  HTML: `<li>
    <a></a>
  </li>`,
  ELEMENT_CLASS: 'menu-option',
  prototype: {
    buttonElement : null,
    init: function(config){
      Widget.prototype.init.call(this, config);
      this.buttonElement = this.element.find('a');
      this.buttonElement.text(config.name);
      this.buttonElement.attr('href', config.route);
    }
  }
});

Class(UI, 'CreatePostController').inherits(Widget)({
  HTML: `<div>
    <form>
      <div class="form-group">
        <label>Write a title:</label>
        <input name="title" class="form-control" />
      </div>
      <div class="form-group">
        <label>Write some text:</label>
        <div id="summernote"></div>
      </div>
      <ul class="nav nav-pills options-menu">
        <li role="presentation" class="active"><button class="btn btn-default post" type="submit">Post</button></li>
        <li role="presentation"><button class="btn btn-default draft" type="submit">Draft</button></li>
        <li role="presentation"><button class="btn btn-default go-back" type="submit">Go Back</button></li>
      </ul>
    </form>
  </div>`,
  ELEMENT_CLASS: 'create_post-component',
  prototype: {
    textEditorElement: null,
    titleEditorElement: null,
    tagsEditorElement: null,
    formElement: null,
    optionsMenuElement: null,
    postButton: null,
    draftButton: null,
    goBackButton: null,
    init: function(config){
      Widget.prototype.init.call(this, config);
      this.titleEditorElement = this.element.find('form  div  input');
      this.textEditorElement = this.element.find('#summernote');
      this.textEditorElement.summernote();
      this.formElement = this.element.find('form');
      this.optionsMenuElement = this.element.find('form > .options-menu');
      this.postButton = this.optionsMenuElement.find('.post');
      this.draftButton = this.optionsMenuElement.find('.draft');
      this.goBackButton = this.optionsMenuElement.find('.go-back');
      //
      var CreatePostController = this;
      var data = {}
      $.get('/user/current_user', function(response){
          data = {
            title: CreatePostController.titleEditorElement.val(),
            content: $(CreatePostController.textEditorElement).summernote('code'),
            tags: '',
            user_id: response.id,
          }
      });
      this.formElement.on('submit', function(event){ console.log("submit"); event.preventDefault(); });
      this.postButton.on('click',function(event){
        event.preventDefault();
          data.published = true;
        $.post('/api/post/new', data, function(response){
          console.log("this will go to the blog post later", response);
        });
      });
      this.draftButton.on('click',function(event){
        event.preventDefault();
          data.published = false;
        $.post('/api/post/new', data, function(response) {
          console.log("this will go to the blog post later", response);
        });
      });



    }
  }
});
var textEditor = new UI.CreatePostController();
textEditor.render($('.create_post'))
var sidebar = new UI.Sidebar();
sidebar.render($('#wrapper'));
