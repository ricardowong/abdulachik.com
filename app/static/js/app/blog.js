
class PostFeed extends React.Component {
  _getPosts(){
    var postFeed = [
      { id: 1,
        title:"tito camotito",
        content: "Lo-fi taxidermy meditation, sartorial ethical master cleanse 8-bit gluten-free venmo vice portland mumblecore stumptown direct trade. Direct trade shabby chic drinking vinegar distillery organic. Single-origin coffee affogato vinyl brunch gentrify fixie. Pork belly typewriter scenester, bitters bushwick migas mustache schlitz. Hammock listicle scenester selvage humblebrag. Trust fund +1 disrupt, kale chips poutine messenger bag shoreditch fixie. Ugh kogi tilde listicle intelligentsia retro.",
        comments: [
          { id:1, author: "obama", body:"well done!", date: "13-10-2019"},
          { id:2, author: "bernie sanders", body:"fuck you obama!", date: "14-10-2019"},
          { id:3, author: "Drumpf", body:"lets make burritos great again!", date: "14-10-2019"}]},
      { id: 2,
        title: "tito malacocico",
        content: "Knausgaard thundercats chicharrones health goth squid normcore. Beard tote bag wayfarers bicycle rights migas, authentic fanny pack meditation you probably haven't heard of them paleo cardigan deep v. Ennui fap godard, banh mi normcore slow-carb bushwick bicycle rights. Umami listicle selvage art party viral, gastropub skateboard dreamcatcher celiac salvia before they sold out cred pop-up keytar locavore. Swag next level gochujang, portland fixie narwhal bushwick chia freegan. Wayfarers everyday carry fanny pack readymade. Hashtag tousled truffaut roof party gochujang.",
        comments:[]}
    ]
    return( postFeed.map(post => <Post title={post.title} content={post.content} comments={post.comments}/> ));
  }
  render() {
    return(
      <div className="contents">
         {this._getPosts()}
      </div>
    );
  }
}

class Post extends React.Component {
  constructor(){
    super();
    this.state = {
      showPost: true
    }
  }
  _handleClick(){
    this.setState({
      showPost: !this.state.showPost
    })
  }

  render(){
    const post = <div className=""><p>{this.props.content}</p><CommentBox comments={this.props.comments}/></div>;
    let postNode;
    let addComentNode;
    if (this.state.showPost){
      postNode = post;
    }
    return(
        <div class="post">
          <div class="text-center">
              <h1 onClick={this._handleClick.bind(this)}>{ this.props.title }</h1>
              <h6>
                  <strong>
                      { this.props.author }
                  </strong>
                  <span class="text-muted">{ this.props.date } </span>
              </h6>

              <a class="btn btn-default" href="#/">
                  <i class="fa fa-arrow-left"></i>  go back
              </a>
          </div>
          <div class="post-body">
              <div ta-bind ng-model="post.content">
                  { this.props.content }
              </div>
          </div>
        </div>

    )
  }
}
class CommentForm extends React.Component{
  _handleSubmit(event){
    event.preventDefault();
    let author = this._author;
    let body = this._body;
    if (!this._author.value || !this._body.value){
      let msg = "Sorry! you need to add " + (!author.value ? "a name " : "") + (!author.value && !body.value ? " and " : "") + (!body.value ? "a message " : "");
      // return(<Notice message={ msg } />);
      alert(msg);
    }
    if(this._getCharacters() < 140  ){
      this.props.addComment(author.value, body.value);
    } else {
      let msg = "Sorry! your message can't be longer than 140 characters"
      // return(<Notice message={msg} />);
      alert(msg);
    }
  }

  _getCharacters(){
    this.setState({
      characters: this._body.value.length
    });
    try{
      return(this.state.characters);
    } catch(error){
      return(0);
    }
  }
  render(){
    return(
      <form className="comment-form full-width-forms" onSubmit={this._handleSubmit.bind(this)}>
        <h4>Submit a comment:</h4>
        <input placeholder="name: " ref={ input => this._author = input }/>
        <textarea placeholder="comment:" ref={ textarea => this._body = textarea } onKeyUp={this._getCharacters.bind(this)}></textarea>
        <button className="btn full blue" type="submit">Submit</button>
      </form>
    )
  }
}
class CommentBox extends React.Component {
  constructor(){
    super();
    this.state = {
      showComments: false,
      comments: this.props ? this.props.comments:[],
      showForm: false
    }
  }
  _handleClick(){
      this.setState({
        showComments: !this.state.showComments
      })
  }
  _getComments(){
    return this.state.comments.map( comment => {
      return (
        <Comment
          author={comment.author}
          body={comment.body}
          key={comment.id}
          />
      )
    })
  }

  _addComment(author, body){
    const comment = {
      id: this.state.comments.length + 1,
      author: author,
      body: body
    };
    this.setState({
      comments: this.state.comments.concat([comment]),
      showForm: false,
      showComments: true
    });
  }

  _showCommentForm(){
    this.setState({
      showForm: !this.state.showForm
    })
  }
  render () {
    let commentsNode, showCommentsNode, commentFormNode, showCommentFormNode;
    if (this.state.showComments){
        commentsNode = this._getComments()
    }
    if (this._getComments().length > 0) {
        showCommentsNode = <div className="row"><button className="btn" onClick={this._handleClick.bind(this)}>Show comments<i className="icon-arrow-updown"></i></button></div>;
    }
    if(this.state.showForm){
        commentFormNode = <CommentForm addComment={this._addComment.bind(this)} />
    } else {
        showCommentFormNode = <div className="row"><button className="btn" onClick={this._showCommentForm.bind(this)}>Add a new Comment</button></div>;
    }

    return(
      <div className="row">
        {showCommentFormNode}
        {commentFormNode}
        {showCommentsNode}
        <div className="col row">{commentsNode}</div>
      </div>
    )
  }
}
class Comment extends React.Component {
  render(){
    console.log(this.props);
    return(
      <div className="row comment">
        <h4>{this.props.author}<small>{this.props.date}</small></h4>
        <p>{this.props.body}</p>
      </div>
    )
  }
}

class Navbar extends React.Component {
  render(){
    return (
      <div className="section">
        <nav className="navbar">
          <ul>
            <li>
              <a href="#">Home</a>
            </li>
            <li>
              <a href="#">Portfolio</a>
            </li>
            <li>
              <a href="#">Contact me</a>
            </li>
            <li>
              <a href="/login">Sign in</a>
            </li>
          </ul>
        </nav>
      </div>
    )
  }
}
class Notice extends React.Component {
  constructor(){
    super();
    this.state = {
      newMessage: false,
      messageQueue: []
    }
  }
  _getMessage(){
    if(this.props.message){
      return(this.props.message);
    }
  }
  render(){
    let MessageNode;
    if(this.state.newMessage){
      MessageNode = this._getMessage()
    }
    return(
      <div className="row notice">
        <div className="section">
          <p>{MessageNode}</p>
          <i className="icon-close-outline"></i>
        </div>
      </div>
    )
  }
}
// let notice = document.getElementById("notice");
let postFeed = document.getElementById("post-feed");
let navbar = document.getElementById("navbar");
// ReactDOM.render(<Notice />, notice);
ReactDOM.render(<Navbar />, navbar);
ReactDOM.render(<PostFeed />, postFeed);
