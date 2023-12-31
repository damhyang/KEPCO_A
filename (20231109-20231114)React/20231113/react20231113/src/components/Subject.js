import React, {Component} from "react";

class Subject extends Component{
    render(){
        return(
            <header>
                <h1><a href="#" onClick={function(e)
                        {
                            this.props.onChangePage();
                            e.preventDefault();
                        }.bind(this)
                }>{this.props.title}</a></h1>
                <h3>{this.props.sub}</h3>
            </header>
        )
    }
}

export default Subject;