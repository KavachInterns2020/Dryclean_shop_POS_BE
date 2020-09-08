import React, { Component } from 'react';
import './login1.css'
import axios from 'axios'

class Login1 extends Component {
   constructor(props){
      super(props);
        this.state={

              email: "",
              password: ""
            
        };
        this.handleInputChange = this.handleInputChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.getCookie = this.getCookie.bind(this)
        
     };

      getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(e){
    e.preventDefault()
    var csrftoken = this.getCookie('csrftoken')
    var url = 'http://127.0.0.1:8000/rest-auth/login/'


    fetch(url, {
            method:'POST',
            headers:{
              'Content-type':'application/json',
              'X-CSRFToken':csrftoken,
              },
              body:JSON.stringify(this.state)
            }).then((response)  => {
                  
                  this.setState({
                    
                        email: "",
                        password: ""
                        
                        
                  })
              }).catch(function(error){
              console.log('ERROR:', error)
            })

    }

   

    
   


	render() { 
  
		return ( 
			<div>
				<section class="login-page">
  	            <form onSubmit={this.handleSubmit} >
  	 	          <div class="box">
					
  	 	 	         <div class="form-head">
  	 	 	   	        <h2>Login</h2>
							   <hr />
							   <br />
					
  	 	 	        </div>
  	 	 	        <div class="form-body">

  	 	 	   	       <input onChange={this.handleInputChange} type="text" name="email" placeholder="Enter email id" name="email" value={this.state.email} />
  	 	 	   	       <input onChange={this.handleInputChange} type="password" name="password" placeholder="Password" name="password" value={this.state.password} />
  	 	 	        </div>
  	 	 	            <div class="form-footer">
								<br />
  	 	 	   	        <button type="submit">LOGIN</button>
						
  	 	 	        </div>
  	 	         </div>
  	           </form>
              </section>

			</div>
		 );
	}
}
 
export default Login1;