import React, { Component } from 'react';
import './customeredit.css'
class CUSTEDIT extends Component {
    state = { 
        prevord : [
            [
                ['pre', "shirt", "iron", "normal", 250, 0, "DONE", 1, 1, 2020, 15, 2, 2020],
                ['pre', "Pant" , "Wash", "Arjent", 300, 0, "DONE", 4, 2, 2020, 20,2, 2020],
           //  item id, item name, service type, priority, paid, pending, status, (3)ordered date, (3)delevered date(date/month/year)
            ],
            [
                ['pre', "Banyana", "Iron", "Normal", 150, 0, "Done", 1, 3, 2020, 20, 3 ,2020],
            ],
            [
               ['pre', "shirt", "iron", "normal", 250, 0, "DONE", 1, 4, 2020, 15, 4, 2020]
            ]
        ],
        presord : [
            [
                ['new', "SHIRT", "WASH", "Normal", 200, 100, "Pending", 12, 6, 2020, 20, 7 , 2020],
                ['new', "JURKUIN","IRON", "Arjent", 0, 500, "Pending", 1, 7, 2020, 25, 7, 2020],
           //  item id, item name, service type, priority, paid, pending, status, (3)ordered date, (3)expected delevery date(date/month/year)
            ],
            [
                ['new', "SAREE", "IRON and WASH", "Normal", 0, 250, "Pending", 5, 7, 2020, 1, 8, 2020],
            ],
        ],
        l : this.props.l,
        s : this.props.s,
        p : this.props.p,
        hh : this.props.o,
        hhh : this.props.e,
     }
    render() { 
        return (  
            <div>
               <p>Item name : {this.state.l}</p>
               <p>Service type : {this.state.s}</p>
              <p> priority : {this.state.p} </p>
              <p>Ordered date : {this.state.hh}</p> 
              <p>Expected Delivery date : {this.state.hhh}</p>

            </div>
        );
    }
}
 
export default CUSTEDIT;