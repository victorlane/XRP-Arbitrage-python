import "./DataGroup.css";
import DataSelection from "./DataSelection.js";


const DataGroup = (props) => {
    const rows = [];
    for(const obj in props.data) {
        rows.push(<DataSelection provider={obj.toUpperCase()} data={props.data[obj]}/>)
    }

    return(
        <div className="data-group">
            {rows}            
        </div>
    )
}

export default DataGroup;