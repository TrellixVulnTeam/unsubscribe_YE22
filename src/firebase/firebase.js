import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore';

// web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDY5l46n0mbnvEJOKJq6rA9OCLTpEHdyGs",
    authDomain: "unsubscribe-69412.firebaseapp.com",
    projectId: "unsubscribe-69412",
    storageBucket: "unsubscribe-69412.appspot.com",
    messagingSenderId: "892250255498",
    appId: "1:892250255498:web:242909766c9f73b4a73d73"
  };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const fbdatabase = firebase.firestore();

export  { fbdatabase }