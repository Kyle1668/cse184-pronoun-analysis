import React, { Component } from "react";
import "./App.css"; /* optional for styling like the :hover pseudo-class */
import USAMap from "react-usa-map";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import { CardHeader } from "@material-ui/core";

const useStyles = makeStyles({
  card: {
    width: 450,
    display: "inline",
    display: "inline-block",
    margin: "15px"
  },
  bullet: {
    display: "inline-block",
    margin: "20px",
    transform: "scale(0.8)"
  },
  title: {
    fontSize: 14,
    height: 150,
    borderBottom: "1px black"
  },
  content: {
    height: 100,
    fontSize: 30
  },
  pos: {
    marginBottom: 12
  }
});

function NationalStatCard(props) {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardHeader className={classes.title} title={props.question} />
      {/* <CardMedia
          className={"test"}
          image="/static/images/cards/paella.jpg"
          title="Paella dish"
        /> */}
      <CardContent className={classes.content}>{props.answer}</CardContent>
    </Card>
  );
}

class PageHeader extends Component {
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

class App extends Component {
  /* mandatory */
  mapHandler = event => {
    alert(event.target.dataset.name);
  };

  /* optional customization of filling per state and calling custom callbacks per state */
  statesCustomConfig = () => {
    return {
      NJ: {
        fill: "navy",
        clickHandler: event =>
          console.log("Custom handler for NJ", event.target.dataset)
      },
      NY: {
        fill: "#CC0000"
      }
    };
  };

  render() {
    return (
      <div className="App">
        <PageHeader />
        <USAMap
          customize={this.statesCustomConfig()}
          onClick={this.mapHandler}
          onHover={console.log("hey")}
        />
      </div>
    );
  }
}

export default App;
