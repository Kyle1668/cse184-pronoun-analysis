import React, { Component } from "react";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import { CardHeader } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

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

export default function NationalStatCard(props) {
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
