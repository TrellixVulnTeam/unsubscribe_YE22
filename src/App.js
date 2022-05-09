import React from 'react';
// import 'bootstrap/dist/css/bootstrap.css';
import { BrowserRouter, Switch, Route} from "react-router-dom";

import 'bootstrap/dist/css/bootstrap.css';

import Home from "./pages/Home";
import Sucess from './pages/Sucess';

function App() {
  
  return (
    <BrowserRouter>

        <Switch>

            <Route exact path='/' component={Home} />
            <Route exact path='/sucess' component={Sucess} />

            {/* <Route exact component={NotFound}/> */}
          </Switch>
    
    </BrowserRouter>
  );
}

export default App;