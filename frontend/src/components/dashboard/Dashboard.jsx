import React from "react";
import { useEffect } from "react";
import { useNavigate } from 'react-router-dom';


export const Dashboard = (props) => {

  const navigate = useNavigate()
  const {
    token,
    setToken
  } = props;
  useEffect(() => {
    if(!token){
      return (navigate("/login"))
    }})

  return (
    <h1> dashboard </h1>
  )
}