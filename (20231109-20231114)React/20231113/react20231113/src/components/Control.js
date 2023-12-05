import React, {Component} from "react";

class Control extends Component{
    render(){
        return(
            <ul>
                <li>
                    <a href="/create" onClick={function(e){
                            e.preventDefault();
                            this.props.onChangemode("create");
                        }.bind(this)}
                    >
                        Create
                    </a>
                </li>
                <li><a href="/update" onClick={function(e){e.preventDefault();
                                                this.props.onChangemode("update")}.bind(this)}>Update</a></li>
                <li><button onClick={function(e){e.preventDefault();
                                                    this.props.onChangemode("delete")}.bind(this)}>Delete</button></li>
            </ul>

        )
    }
}

export default Control;