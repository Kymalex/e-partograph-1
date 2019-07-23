# app/admin/views.py

# 3rd party imports
from flask import render_template, flash, redirect, url_for, request

# local imports
from app.admin import admin
from app.models import Nurse, Ward, Patient
from app.admin.forms import CreateNurseForm, CreateWardForm, CreatePatientForm

@admin.route('/admin/create-nurse', methods=['GET', 'POST'])
def create_nurse():
  '''
  creates a new Nurse
  '''
  form = CreateNurseForm()
  if request.method == 'POST':
    if form.validate_on_submit:
      nurse = Nurse.query.filter_by(email = form.email.data).first()
      if nurse is None:
        nurse = Nurse(
          firstname = form.firstname.data,
          lastname = form.lastname.data,
          email = form.email.data,
          phone_no = form.phone_no.data,
          password = form.password.data
        )
        nurse.save()
        flash('Successfully created a new user')
        return redirect(url_for('admin.nurses'))
      else:
        flash('User exists please try again')

  return render_template('admin/create-nurse.html', title='Nurses', form=form)

@admin.route('/admin/create-ward', methods=['GET', 'POST'])
def create_ward():
  '''
  creates a new Ward
  '''

  form = CreateWardForm()

  if request.method == 'POST':
    if form.validate_on_submit:
      ward = Ward.query.filter_by(name = form.name.data).first()
      if ward is None:
        ward = Ward(
          name = form.name.data,
          beds = form.beds.data,
          nurse_id = form.nurse_id.data
        )
        ward.save()
        flash('Successfully created a new ward')
      return redirect(url_for('admin.wards'))
    else:
      flash('Ward already exists')

  return render_template('admin/create-ward.html', title='Wards', form=form)

@admin.route('/admin/wards')
def wards():
  '''
  view wards in the system
  '''

  wards = Ward.query.all()

  return render_template('admin/view-wards.html', title='Wards', wards=wards)

@admin.route('/admin/profile')
def profile():
  '''
  display the admin info
  '''

  return render_template('admin/profile.html', title='Profile')

@admin.route('/admin/nurses')
def nurses():
  '''
  display the nurses in the system
  '''

  nurses = Nurse.query.all()

  return render_template('admin/view-nurses.html', title='Nurses', nurses=nurses)

@admin.route('/admin/patients')
def patients():
  '''
  display the patients in the system
  '''

  patients = Patient.query.all()

  return render_template('admin/view-patients.html', title='Patients', patients=patients)

@admin.route('/admin/create-patient')
def create_patient():
  '''
  Creates a new patient
  '''
  form = CreatePatientForm()
  if request.method == 'POST':
    if form.validate_on_submit:
      patient = Patient.query.filter_by(email = form.email.data).first()
      if patient is None:
        patient = Patient(
          firstname = form.firstname.data,
          lastname = form.lastname.data,
          dob = form.dob.data,
          email = form.email.data,
          phone_no = form.phone_no.data,
          id_no = form.id_no.data,
          nhif_no = form.nhif_no.data,
          ward_id = form.ward_id.data
        )
        patient.save()
        flash('Successfully created a new patient')
        return redirect(url_for('admin.patients'))
      else:
        flash('Patient exists')
  return render_template('admin/create-patient.html', title='Patients', form=form)

