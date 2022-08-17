import React from "react";
import { Routes as RouteList, Route, Navigate } from "react-router-dom";
import {
  Main,
  Finish,
} from "./views";

interface Props {
  path: string;
  exact?: boolean;
  auth?: boolean;
  component: any;
  layout: any;
}

const Routes: React.FC = () => {
  return (
    <RouteList>
      <Route path="/" element={<Navigate replace to="/main" />} />
      <Route path="/main" element={<Main />} />
      <Route path="/finish" element={<Finish />} />
      <Route element={<Navigate replace to="/not-found" />} />
    </RouteList>
  );
};

export default Routes;
