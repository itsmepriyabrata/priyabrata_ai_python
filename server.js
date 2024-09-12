const express = require('express');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const cookieSession = require('cookie-session');
const cors = require('cors');

// Initialize the express app
const app = express();

// Middleware for sessions
app.use(cookieSession({
  name: 'session',
  keys: ['key1', 'key2']
}));

// Initialize Passport and sessions
app.use(passport.initialize());
app.use(passport.session());
app.use(cors());

// Define callback URL based on environment (production or development)
const callbackURL = process.env.NODE_ENV === 'production'
  ? 'https://recorder-back-7sml.onrender.com/auth/google/callback'  // Use your actual production domain here
  : 'http://localhost:6005/auth/google/callback';  // Development URL for local testing

// Passport configuration for Google OAuth 2.0
passport.use(new GoogleStrategy({
     clientID: '',  // Replace with your Google Client ID
     clientSecret: '',  // Replace with your Google Client Secret
     callbackURL: callbackURL
  },
  function(accessToken, refreshToken, profile, done) {
    return done(null, profile);
  }
));

// Serialize user into the session
passport.serializeUser((user, done) => {
  done(null, user);
});

// Deserialize user out of the session
passport.deserializeUser((user, done) => {
  done(null, user);
});

// Google OAuth login route
app.get('/auth/google',
  passport.authenticate('google', { scope: ['profile', 'email'] })
);

// Google OAuth callback route
app.get('/auth/google/callback', 
  passport.authenticate('google', { failureRedirect: '/login' }),
  (req, res) => {
    res.redirect('http://localhost:3000');  // Redirect to React app after login
  }
);

// Route to get the current logged-in user
app.get('/api/current_user', (req, res) => {
  if (req.isAuthenticated()) {
    res.send(req.user);
  } else {
    res.status(401).send('Not authenticated');
  }
});

// Logout route
app.get('/logout', (req, res) => {
  req.logout();
  res.redirect('/');
});

// Start the server
app.listen(6005, () => {
  console.log('Server started on http://localhost:6005');
});
