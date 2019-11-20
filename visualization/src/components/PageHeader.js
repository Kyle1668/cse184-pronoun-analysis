import React, { Component } from "react";
import NationalStatCard from "./NationalStatCard";
import "../styles/PageHeader.css";
import data from "../fake-data.json";

export default class PageHeader extends Component {
  render() {
    return (
      <div className="page-header">
        <h1>Gendered Job Posting Analysis</h1>
        {data.USA.map(element => {
          return (
            <NationalStatCard
              question={element.question}
              answer={element.answer}
            />
          );
        })}
      </div>
    );
  }
}
