import React from "react";
import { Route, Routes } from 'react-router-dom';
import { ErrorPage } from "./ErrorPage";
import { PageNotFound } from "./PageNotFound";

export const ErrorRouter = ({ defaultPage }) => {
  
  return (
    <Routes>
      <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>
      <Route index path="login" element={<ErrorPage redirect={defaultPage} />} />
      <Route path="database" element={<ErrorPage redirect={defaultPage}/>} />
    </Routes>   
  )
}