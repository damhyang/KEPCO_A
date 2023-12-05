import React, {Component} from 'react';

class Child extends Component {
      render() {
        return (
          <div>
            {/* <p>1</p>
            <p>2</p> */}
            <p>{this.props.a}</p>
            <p>{this.props.b}</p>
          </div>
        )
      }
    }

export default Child;