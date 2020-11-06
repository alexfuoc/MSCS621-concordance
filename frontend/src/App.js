import "./App.css";
import React, { Component } from "react";

export class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: "",
      concordanceResponse: null,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event) {
    alert("A name was submitted: " + this.state.value);
    fetch("http://localhost:8080/mscs721/concordance/1.0.0/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(this.state.value),
    })
      .then((response) => {
        console.log(response);
        response.json();
      })
      .then((result) => {
        console.log("Success:", result);
        this.setState({ concordanceResponse: result });
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    event.preventDefault();
  }

  render() {
    const { concordanceResponse } = this.state;
    return (
      <div className="App App-center">
        <h1>Concordance Application</h1>
        <p>Input text to be analyzed:</p>
        <form onSubmit={this.handleSubmit}>
          <input
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
          />
          <input type="submit" value="Submit" />
        </form>
        <hr />
        {concordanceResponse !== null && <p>{concordanceResponse}</p>}
      </div>
    );
  }
}

export default App;
