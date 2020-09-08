import React, { Component } from 'react';
import OrderTaken from './ordertaken';
import Settings from './settings';

class Storage extends Component {
    state = { 
        list : ['choose', 'shirt', 'pant', 'lungi', 'banyan'],
        servicetype : ['choose', 'IRON', 'WASH', 'DRY'],
        priority : ['choose', 'normal', 'arjent'],
        ord : "false",
        set : "true"
     }
     handleAdd = (item) => {
         this.setState({list: this.state.list.concat(item) });
     }
    render() { 
        return ( 
            <div>
                {this.set === "true" ? <Settings list = {this.state.list} servicetype = {this.state.servicetype} priority = {this.state.priority} 
                onAdd = {this.handleAdd} pq={"true"}>
                </Settings> :
                <Settings list = {this.state.list} servicetype = {this.state.servicetype} priority = {this.state.priority} 
                onAdd = {this.handleAdd} pq={"false"}></Settings>  }    
            </div>
         );
    }
}
 
export default Storage;