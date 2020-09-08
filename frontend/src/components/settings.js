import React, { Component } from 'react';
import OrderTaken from './ordertaken';
import {Link, Router} from 'react-router-dom';
import "./settings.css"

class Settings extends Component {
    state = { 
        list : ['choose', 'shirt', 'pant', 'lungi', 'banyan'],
        servicetype : ['choose', 'IRON', 'WASH', 'DRY'],
        priority : ['choose', 'normal', 'arjent'],
        name : '',
        pq : this.props.pq,
     }
     getInputValue = (event) => {
        this.setState({
            name : event.target.value
        })
        
    }
    AddItem = () =>{
       const newItem = this.state.name;
       this.setState({ list: this.state.list.concat(newItem)})
    }

    deleteItem = (id) =>{
        const list = Object.assign([], this.state.list);
        list.splice(id,1);
        this.setState({list: list})
    }

    getInputValue1 = (event) => {
        this.setState({
            name : event.target.value
        })
        
    }
    AddItem1 = () =>{
       const newItem = this.state.name;
       this.setState({ servicetype: this.state.servicetype.concat(newItem)})
    }

    deleteItem1 = (id) =>{
        const servicetype = Object.assign([], this.state.servicetype);
        servicetype.splice(id,1);
        this.setState({servicetype: servicetype})
    }

    getInputValue11 = (event) => {
        this.setState({
            name : event.target.value
        })
        
    }
    AddItem11 = () =>{
       const newItem = this.state.name;
       this.setState({ priority: this.state.priority.concat(newItem)})
    }

    deleteItem11 = (id) =>{
        const priority = Object.assign([], this.state.priority);
        priority.splice(id,1);
        this.setState({priority: priority})
    }
    render() { 
        return ( 
            <div>
                {this.state.pq==="true" ? <OrderTaken list = {this.state.list} servicetype = {this.state.servicetype} priority = {this.state.priority}>
                                 </OrderTaken> :
                 <div>
                 <div class="row">
                 <div class="column">
                 <input type="text" onChange={this.getInputValue} placeholder="add new element" ></input>
                 <button className="btn btn-success" onClick={ this.AddItem }>ADD NEW ITEM</button>
                 <ul>
                     {this.state.list.map((item, index) => <ol key={index} >{item}
                     <button onClick={() => this.deleteItem(index)}> X </button> </ol>)}
                 </ul>
                 </div>
                 <div class="column">
                 <input type="text" onChange={this.getInputValue1} placeholder="add new element" ></input>
                 <button className="btn btn-success" onClick={ this.AddItem1 }>ADD NEW servicetype</button>
                 <ul>
                     {this.state.servicetype.map((item, index) => <ol key={index} >{item}
                     <button onClick={() => this.deleteItem1(index)}> X </button> </ol>)}
                 </ul>
                 </div>
                 <div class="column">
                 <input type="text" onChange={this.getInputValue11} placeholder="add new element" ></input>
                 <button className="btn btn-success" onClick={ this.AddItem11 }>ADD NEW priority</button>
                 <ul>
                     {this.state.priority.map((item, index) => <ol key={index} >{item}
                     <button onClick={() => this.deleteItem11(index)}> X </button> </ol>)}
                 </ul>

                 <Link to="/" class="btn btn-info">SAVE & SUBMIT</Link>
                 </div>
                 </div>
                 </div>
                 }
            </div>
         );
    }
    
}
 
export default Settings;