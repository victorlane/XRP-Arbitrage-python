import "./DataSelection";
import DataBox from "./DataBox.js";

const DataSelection = props => {
    const rows = [];
    const provider = props.provider;
    for(const obj in props.data) {
        rows.push(<DataBox currency={obj} value={props.data[obj]}/>)
    }
    return (
        <div>
             <div className="data-text">
                <div className="data-provider">{provider}</div>
            </div>
            {rows}
        </div>
    )
}

export default DataSelection;