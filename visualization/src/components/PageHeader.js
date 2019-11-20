import React, { Component } from "react";
import NationalStatCard from "./NationalStatCard";
import data from "../data.json";

export default class PageHeader extends Component {
  render() {
    return (
      <div className="page-header">
        <h1>Gendered Job Posting Analysis</h1>
        <NationalStatCard
          question="What percentage have gender pronouns in the job posting?"
          answer="15%"
        />
        {/* <NationalStatCard question="How are gendered job postings distributed across the USA?" answer="lorem ipsum" /> */}
        <NationalStatCard
          question="What are the most common roles in tech that have gendered job postings?"
          answer="SWE, PM, and CTO"
        />
        <NationalStatCard
          question="Out of the gendered words/phrases, which are the most common? "
          answer="hacker, ninja, dominate"
        />
      </div>
    );
  }
}
