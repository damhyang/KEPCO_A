import React, {Component} from "react";

class TOC extends Component{
    render(){
        const lists=[];
        for (let i=0; i<this.props.contents.length; i++){
            const content=this.props.contents[i];
            lists.push(
                <li key={content.id}>
                    <a href={'/content/'+content.id} 
                        onClick={
                            function(e){
                                e.preventDefault(); 
                                this.props.onSelect(content.id);
                            }.bind(this)
                    }>
                        {content.title}
                    </a>
                </li>
            );
        }
        return(
            <nav>
               {lists}
            </nav>
        )
    }
}

export default TOC;