import React, { Component } from 'react'
import './customer.css'
import {Link, Router} from 'react-router-dom';
import collapsible from 'react-collapsible';
import Collapsible from 'react-collapsible';

class CUSTOMER extends Component {
    state = { 
         prevord : [
             [
                 ["shirt", "iron", "normal", 200,"DONE", "2020/01/05","2020/06/08"],
                 [ "Pant" , "Wash", "Arjent", 150,"DONE", "2020/06/04", "2020/08/03"],
            //  item id, item name, service type, priority, paid, pending, status, (3)ordered date, (3)delevered date(date/month/year)
             ],
             [
                ["shirt", "iron", "normal", 300,"DONE", "2020/01/05","2020/06/08"],
             ],
             [
                ["shirt", "iron", "normal", 250,"NOT", "2020/01/05","2020/06/08"],
             ],
             [
                ["shirt", "iron", "normal", 100,"DONE", "2020/01/05","2020/06/08"],
                ["shirt", "iron", "normal", 250,"NOT", "2020/01/05","2020/06/08"],
            //  item id, item name, service type, priority, paid, pending, status, (3)ordered date, (3)expected delevery date(date/month/year)
             ],
             [
                ["shirt", "iron", "normal", 250,"NOT", "2020/01/05","2020/06/08"],
             ],
            ],
            pp : 1,
         
         }
  
    openNav = () =>{
        document.getElementById("myNav").style.height = "100%";
    }
    closeNav = () =>{
        document.getElementById("myNav").style.height = "0%";
    }
    mycontent = () =>{
        var m = document.getElementById("content0");
        var x = document.getElementById("content");
        var y = document.getElementById("content1");
        var z = document.getElementById("content2");
        if(x.style.display === "none"){
            x.style.display="block";
            y.style.display ="none";
            m.style.display = "none";
            z.style.display = "none";
        }
        else{
            x.style.display = "none";
            y.style.display = "none";
            m.style.display = "block";
            z.style.display = "none";
        }
    }
    mycontent1 = () => {
        var m = document.getElementById("content0");
        var x = document.getElementById("content");
        var y = document.getElementById("content1");
        var z = document.getElementById("content2");
        if(y.style.display === "none"){
            y.style.display="block";
            x.style.display="none";
            m.style.display = "none";
            z.style.display = "none";
        }
        else{
            x.style.display = "none";
            y.style.display = "none";
            m.style.display = "block";
            z.style.display = "none";
        }
    }
    mycontent2 = () => { 
         var m = document.getElementById("content0");
         var x = document.getElementById("content");
         var y = document.getElementById("content1"); 
         var z = document.getElementById("content2");

         if(z.style.display ==="none")
         {
            y.style.display="none";
            x.style.display="none";
            m.style.display = "none";
            z.style.display = "block";
         }
         else{
            x.style.display = "none";
            y.style.display = "none";
            m.style.display = "block";
            z.style.display = "none";
         }
    }

    changer = (item) =>{
       let am = 0;
       let newo = item.map(v => {
           if(v[3])
           {
             am = am + v[3];
           }
           else{
             
           }
       })
       return am;
    }
    changerone = (item) => {
        var x = 0;
        var y = item.length;
        let newo = item.map(v => {
            if(v[4]==="DONE")
            {
                x = x+1;
            }
        })
        if(x===y)
        {
            return 1;
        }
        else{
            return 0;
        }
    }

    render() { 
        return (
            <div>
                
                 <nav class="navbar navbar-inverse">
                    <div class="container">
                      <div class="navbar-header">
                          <button type="button" class="navbar-toggle collapsed"  onClick={this.openNav} aria-expanded="false">
                              <span class="icon-bar"></span>
                              <span class="icon-bar"></span>
                              <span class="icon-bar"></span>
                          </button>
                         <a href="#" class="navbar-brand"><span class="glyphicon glyphicon-picture" aria-hidden="true"></span>DRY-CLEAN</a>
                         <h2 class="navbar-brand"><strong><em>CUSTOMERS</em></strong></h2>
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
                   <div id="myNav" class="overlay">
                           <a href="javascript:void(0)" class="closebtn" onClick={this.closeNav} >&times;</a>
                           <div class="overlay-content">
                               <Link to="/">HOME</Link>
                               <Link to="/dashboard">DASH BOARD</Link>
                               <Link to="/ordertaken">ORDER TAKEN</Link>
                               <Link to="/customer">CUSTOMERS</Link>
                               <Link to="/employees">EMPLOYEES</Link>
                               <Link to="#">TRANSACTION</Link>
                               <Link to="#">REPORTS</Link>
                           </div>
                   </div>
                </nav>
                 <div class="split on left" id="section-1">
                     <div class="pp">
                         <img src="" alt=""></img>
                         <h2>Shivakumar</h2>
                         <p>Some text ...</p>
                     </div>
                     <div class="centered">
                         <button onClick={this.mycontent}  class="btn btn-lg btn-primary bg-transparent">PRESENT ORDER</button>
                         <br></br>
                         <br></br>
                         <button onClick={this.mycontent1}  class="btn btn-lg btn-primary">PREVIOUS ORDER</button>
                         <br></br>
                         <br></br>
                         <button onClick={this.mycontent2} class="btn btn-lg btn-primary">ALL TRANSACTIONS</button>
                         <br/>
                         <br/>
                         <Link to="/customeredit"><button class="btn btn-lg btn-primary">CUSTOMER EDIT</button></Link>
                     </div>
                 </div>
                 <div class="main" id="section-2">
                 <div class="split re right" id="content0">
                     <h1 class="pp">
                         WELCOME
                     </h1>
                    <div class="centered">
                        <h1>PPSS Dry-cleaner</h1>
                    </div>
                 </div>
                 <div class = "split re right" id="content">
                 <ul>
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                              {
                                 (!this.changerone(item) ? 
                                  <Collapsible  trigger={<div class="oval1">Present {ind + 1}</div>}>
                                     <div class="view">
                                        <ul class="oo">
                                            {item.map((value,index) => <ol key={index}>
                                              <Collapsible  trigger={<button class="btn btn-ifo">item id :custID.{ind +1}.{index+1}</button>}>
                                                <p>Ordered item id : </p>
                                                <p>Ordered date :  {value[5]}</p>
                                                <p>Item Name : {value[0]}</p>
                                                <p>Service Type : {value[1]}</p>
                                                <p>Priority : {value[2]}</p>
                                                <p>Amount : <strong>{value[3]}</strong></p>
                                                
                                                <p><button class="btn btn-primary">{value[4]}</button></p>
                                                <p>Expected Delivery date :  {value[6]}</p>
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible> : null) }
                                 <br />
                                 
                         </ol>)}
                           <br/>
                           <br/>
                           <br/>
                     </ul>
                 </div>
                 <div class = "split re right" id="content1">
                     <ul>
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                                     {
                                         (this.changerone(item) ? 
                                  <Collapsible  trigger={<div class="oval2"><p>Previous</p>{ind + 1}</div>}>
                                     <div class="view">
                                        <ul>
                                            {item.map((value,index) => <ol class="oo"key={index}>
                                            <Collapsible  trigger={<button class="btn btn-ifo">item id :custID.{ind +1}.{index+1}</button>}>
                                                <p>Ordered item id : </p>
                                                <p>Ordered date :  {value[5]}</p>
                                                <p>Item Name : {value[0]}</p>
                                                <p>Service Type : {value[1]}</p>
                                                <p>Priority : {value[2]}</p>
                                                <p>Amount : <strong>{value[3]}</strong></p>
                                                
                                                <p><button class="btn btn-primary">{value[4]}</button></p>
                                                <p>Expected Delivery date :  {value[6]}</p>
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible>
                                : null)
                                }
                                 <br />
                                 
                         </ol>)}
                           <br />
                           <br/>
                           <br/>
                     </ul>
                                     
                 </div>
                 <div class = "split re right" id="content2">
                     <ul>
                      
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                              {
                                  (this.changerone(item) ?
                                  <Collapsible  trigger={<div class="oval2"><p>previous</p>{ind + 1}</div>}>
                                     <div class="view">
                                        <ul>
                                            {item.map((value,index) => <ol class="oo"key={index}>
                                              <Collapsible  trigger={<button class="btn btn-ifo">item id :custID.{ind+1}.{index+1}</button>}>
                                               
                                                <p>{value[4]} </p>
                                               
                                                 
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible> : null )}
                                 <br />
                                 
                         </ol>)}
                           
                     </ul>
                     <ul>
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                             {
                                  (!this.changerone(item) ?
                                  <Collapsible  trigger={<div class="oval1"><p>Present</p>{ind + 1}</div>}>
                                     <div class="view">
                                        <ul class="oo">
                                            {item.map((value,index) => <ol key={index}>
                                              <Collapsible  trigger={<button class="btn btn-ifo">item id :custID.{ind +1}.{index+1}</button>}>
                                                
                                                <p>{value[4]}</p>
                                                
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible>:null)}
                                 <br />
                                 
                         </ol>)}
                        <br/>
                        <br/>
                        <br/>
                     </ul>                 
                 </div>
                 </div>
            </div>
         );
    }
    
    
}
 
export default CUSTOMER;

/*
  <div class="main" id="section-2">
                 <div class="split re right" id="content0">
                     <h1 class="pp">
                         WELCOME
                     </h1>
                    <div class="centered">
                        <h1>PPSS Dry-cleaner</h1>
                    </div>
                 </div>
                 <div class = "split re right" id="content">
                 <ul>
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                                  <Collapsible  trigger={<div class="oval1">Present {ind + 1}</div>}>
                                     <div class="view">
                                        <ul class="oo">
                                            {item.map((value,index) => <ol key={index}>
                                             
                                              <Collapsible  trigger={<button class="btn btn-ifo">item id :{ind +1}.{index+1}</button>}>
                                                <p>Ordered item id : </p>
                                                <p>Ordered date :  </p>
                                                <p>Item Name : {value[0]}</p>
                                                <p>Service Type : {value[1]}</p>
                                                <p>Priority : {value[2]}</p>
                                                <p>Amount : <strong>{value[3]}</strong></p>
                                                
                                                <p><button class="btn btn-primary">{value[4]}</button></p>
                                                <p>Expected Delivery date :  </p>
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible>
                                 <br />
                                 
                         </ol>)}
                           
                     </ul>
                 </div>
                 <div class = "split re right" id="content1">
                     <ul>
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                              
                                  <Collapsible  trigger={<div class="oval2"><p>Previous</p>{ind + 1}</div>}>
                                     <div class="view">
                                        <ul>
                                            {item.map((value,index) => <ol class="oo"key={index}>
                                            <Collapsible  trigger={<button class="btn btn-ifo">item id :{ind +1}.{index+1}</button>}>
                                                <p>Ordered item id : </p>
                                                <p>Ordered date :  </p>
                                                <p>Item Name : {value[0]}</p>
                                                <p>Service Type : {value[1]}</p>
                                                <p>Priority : {value[2]}</p>
                                                <p>Amount : <strong>{value[3]}</strong></p>
                                                
                                                <p><button class="btn btn-primary">{value[4]}</button></p>
                                                <p>Expected Delivery date :  </p>
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible>
                                 <br />
                                 
                         </ol>)}
                           
                     </ul>
                                     
                 </div>
                 <div class = "split re right" id="content2">
                     <ul>
                      
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                              
                                  <Collapsible  trigger={<div class="oval2"><p>previous</p>{ind + 1}</div>}>
                                     <div class="view">
                                        <ul>
                                            {item.map((value,index) => <ol class="oo"key={index}>
                                              <Collapsible  trigger={<button class="btn btn-ifo">item id :{ind+1}. {value[0]}.{index+1}</button>}>
                                               
                                                <p>Paid </p>
                                               
                                                 
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible>
                                 <br />
                                 
                         </ol>)}
                           
                     </ul>
                     <ul>
                         {this.state.prevord.map((item,ind) => <ol key={ind}>
                              
                                  <Collapsible  trigger={<div class="oval1"><p>Present</p>{ind + 1}</div>}>
                                     <div class="view">
                                        <ul class="oo">
                                            {item.map((value,index) => <ol key={index}>
                                              <Collapsible  trigger={<button class="btn btn-ifo">item id :{ind +1}. {value[0]}.{index+1}</button>}>
                                                
                                                <p>paid</p>
                                                
                                                </Collapsible>
                                                <br />
                                            </ol>)}
                                        </ul>
                                     </div>
                                 </Collapsible>
                                 <br />
                                 
                         </ol>)}
                           
                     </ul>                 
                 </div>
                 </div>*/
