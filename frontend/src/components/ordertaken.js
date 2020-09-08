import React, { Component } from 'react';
import './ordertaken.css';
import {Link, Router} from 'react-router-dom';
import CUSTEDIT from './customeredit';


class OrderTaken extends Component {
    state = {  
        list : this.props.list,
        servicetype :this.props.servicetype,
        priority : this.props.priority,
        servicevalue : "choose",
        listvalue : "choose",
        priorityvalue : "choose",
        isSubmitted: false,
        hh : '',
        hhh : '',
    }
    handleServicetype = event => {
        this.setState({
            servicevalue : event.target.value
        })
    }
    handleAdditem = event =>{
        this.setState({
            listvalue : event.target.value
        })
    }
    handlePriority = event => {
        this.setState({
            priorityvalue : event.target.value
        })
    }
   
    handleSubmit = event => {
        //alert(`${this.state.listvalue} ${this.state.servicevalue} ${this.state.priorityvalue} `)
        this.setState({
            isSubmitted:true,
        })
    }
    handledate = event =>{
        this.setState({
            hh : event.target.value
        })
    }
    handleexpdate = event =>{
        this.setState({
            hhh : event.target.value
        })
    }
    mycontent = () =>{
           var x = document.getElementById("content-1");
           var y = document.getElementById("content-2");

           x.style.display = "none";
           y.style.display = "block";
    }
    mycontent1 = () =>{
        var x = document.getElementById("content-1");
        var y = document.getElementById("content-2");

        x.style.display = "block";
        y.style.display = "none";
    }

    render() { 
        return ( 

            <div id="main">
                {this.state.isSubmitted ? <CUSTEDIT l = {this.state.listvalue} s = {this.state.servicevalue} p = {this.state.priorityvalue} o ={this.state.hh} e = {this.state.hhh} /> : <div>
                <nav class="navbar navbar-inverse">
                    <div class="container">
                      <div class="navbar-header">
                          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-nav-demo" aria-expanded="false">
                              <span class="icon-bar"></span>
                              <span class="icon-bar"></span>
                              <span class="icon-bar"></span>
                          </button>
                         <a href="#" class="navbar-brand"><span class="glyphicon glyphicon-picture" aria-hidden="true"></span>DRY-CLEAN</a>
                         <h2 class="navbar-brand"><strong><em>ORDER TAKEN</em></strong></h2>
                      </div>
                      <div class="collapse navbar-collapse" id="bs-nav-demo">
                        <ul class="nav navbar-nav">
                            <li><Link to="/">HOME</Link></li>
                            <li><Link to="/dashboard">DASH BOARD</Link></li>
                            <li><Link to="/ordertaken">ORDER TAKEN</Link></li>
                            <li><Link to="/customer">CUSTOMERS</Link></li>
                            <li><Link to="/employees">EMPLOYEES</Link></li>
                            <li><Link to="#">TRANSACTION</Link></li>
                            <li><Link to="#">REPORTS</Link></li>
                        </ul>
                      </div>
                   </div>
                </nav>
               <div id = "content-1">
                  
                     <button class="btn btn-info">Add new customer</button>

                     <button onClick={this.mycontent}  class="btn  btn-primary bg-transparent ">ADD ITEM</button>
               </div>
               <div id = "content-2">
                <form onSubmit={this.handleSubmit}>
                <label for="Additem">ADD ITEM</label>
                <select id="Additem" value={this.state.listvalue} onChange={this.handleAdditem}>
                    {this.state.list.map(function(item){
                        return <option key={item} value={item}>{item}</option>
                    })}
                </select>
               
                <br />
                <br />
                <label for="servicetype">SERVICE TYPE</label>
                <select id="servicetype" value={this.state.servicevalue} onChange={this.handleServicetype}>
                    {this.state.servicetype.map(function(item){
                        return <option key={item} value={item}>{item}</option>
                    })}
                </select>
                <br />
                <br />
                <label for="priority">PRIORITY</label>
                <select id="priority" value={this.state.priorityvalue} onChange={this.handlePriority}>
                    {this.state.priority.map(function(item){
                        return <option key={item} value={item}>{item}</option>
                    })}
                </select>
                <br/>
                <label>Order date</label><input type ="date" value={this.state.hh} onChange={this.handledate}></input>
                <br />
                <label>Expected Delivery</label><input type="date" value={this.state.hhh} onChange={this.handleexpdate}></input>
                <h1>{this.state.hh}</h1>
                <br />
                
                <br />
                 
                <input class="btn btn-primary" type="submit"></input>
                
                </form>
                      <button onClick={this.mycontent1}  class="btn btn-lg btn-primary bg-transparent">Previous page</button>
                </div>
                </div>}
           </div>
         );
    }
    
  
}

 
export default OrderTaken;