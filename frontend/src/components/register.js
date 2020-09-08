import React, { Component } from 'react';

import './register.css';

class Register extends Component{
 constructor(props){
  super(props);
    this.state={

          email: "",
          shop_name:"",
          contact_name:"",
          phone:"",
          shop_address:"",
          gst_number:"",
          password1: "",
          password2: ""
        
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
    var url = 'http://127.0.0.1:8000/rest-auth/registration/'


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
                        shop_name:"",
                        contact_name:"",
                        phone:"",
                        shop_address:"",
                        gst_number:"",
                        password1: "",
                        password2: ""
                        
                        
                  })
              }).catch(function(error){
              console.log('ERROR:', error)
            })

    }


    render(){

    
      return ( 
            <div>
                 <section class="login-page">
                <form onSubmit={this.handleSubmit}>
                <div class="box">
          
                 <div class="form-head">
                    <h2> Register</h2>
                 <hr />
          </div>

                <div class="form-body">
                    <div class="row">
                   <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"><input onChange={this.handleInputChange} type="text" placeholder="Enter shop name" name="shop_name" value={this.state.shop_name} /></div>
                       <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"><input onChange={this.handleInputChange} type="email" placeholder="Enter email id" name="email" value={this.state.email} /></div>
                    </div>
                    <div class="row">
                        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"><input onChange={this.handleInputChange} type="number" placeholder="Enter phone number" name="phone" value={this.state.phone} /></div>
                        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"><input onChange={this.handleInputChange} type="text" placeholder="Enter contact name " name="contact_name" value={this.state.contact_name} /></div>
                    </div>
                    <div class="row">
                       <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"><input onChange={this.handleInputChange} type="Password" placeholder="Enter password" name="password1" value={this.state.password1} /></div>
                       <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"><input onChange={this.handleInputChange} type="password" placeholder="Re-enter password" name="password2" value={this.state.password2} /></div>
                   </div>
                    <div class="row">
                        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"><input onChange={this.handleInputChange} type="text" placeholder="Gst number" name="gst_number" value={this.state.gst_number} /> </div>
                       <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12"> <input onChange={this.handleInputChange} type="text-area" placeholder="Enter  shop addres here" name="shop_address" value={this.state.shop_address}  ></input></div>
                    </div>
                    <br />
                    
                   
                </div>
                    <div class="form-footer">
                <br />
                    <button type="submit">Register</button>
            
                </div>
               </div>
               </form>
              </section>
            </div>

         );
    }
  
}

 
export default Register;