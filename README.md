<img width="1672" alt="FlufflyLove Preview" src="/preview.png">

# FluffyLove.Pet - A Adoption App

Welcome to the FluffyLove Pet Adoption App!
This Flask-based web application allows users to view and interact with a database of pets available for adoption.
Users can browse pets, view details, add new pets, edit existing pet information, and sign up for an account.

## Features

### Home Page

- The home page displays a list of all available pets.
- Each pet's name, species, and availability status are visible.

### Pet Details

- Clicking on a pet's name or ID navigates to a page showing detailed information about that specific pet.
- The pet's photo, species, age, availability, and notes are displayed.

### Filter by Species

- Users can filter pets by species by navigating to `/species_name`.
- This page displays a list of pets belonging to the specified species.

### Edit Pet

- Users can edit a pet's information by clicking on the "Edit" button on the pet details page.
- The edit form pre-populates with the existing information, and users can make changes and save them.

### Delete Pet

- Users can delete a pet by clicking on the "Delete" button on the pet details page.
- A confirmation message appears, and upon confirmation, the pet is removed from the database.

### Add Pet

- Users can add a new pet to the database by navigating to the `/add` page.
- The "Add Pet" form requires details such as name, species, photo URL, age, availability, and notes.

### User Signup

- Users can sign up for an account by navigating to the `/signup` page.
- The signup form collects information such as username, first name, and last name.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Flask
- SQLAlchemy
- PostgreSQL

## Setup

1. Clone the repository.
2. Create a PostgreSQL database named `fluffylove`.
3. Update the `SQLALCHEMY_DATABASE_URI` in the `app.py` file to match your database connection.
4. Run the application using `python app.py`.

## Dependencies

- Flask
- Flask-SQLAlchemy

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- Samie Smilz

Thank you for using the FluffyLove Pet Adoption App!
