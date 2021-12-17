import "./DataBox.css";

const DataBox = props => {
    return (
        <div className="data-box-parent">
            <div className="data-box">
                <div className="data-currency">{props.currency}</div>
                <div className="data-value">{props.value.toFixed(3)}</div>
            </div>
        </div>
    )
}

export default DataBox;