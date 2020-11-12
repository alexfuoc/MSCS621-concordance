import "./App.css";
import services from "./services";
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
    fetch(`${services.host}/mscs721/concordance/1.0.0/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "text/plain",
      },
      body: JSON.stringify(this.state.value),
    })
      .then((res) => {
        console.log(res);
        console.log(res.text);
        return res.text();
      })
      .then((body) => {
        try {
          return JSON.parse(body);
        } catch {
          return { error: "Error: Try again" };
        }
      })
      .then((res) => {
        console.log("Success:", res);
        this.setState({ concordanceResponse: res });
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
        {concordanceResponse && <p>{JSON.stringify(concordanceResponse)}</p>}
      </div>
    );
  }
}

export default App;
