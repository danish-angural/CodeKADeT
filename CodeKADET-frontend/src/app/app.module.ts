import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { MatToolbarModule } from '@angular/material/toolbar';
import { AceEditorModule } from 'ng2-ace-editor';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input'
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSidenavModule } from '@angular/material/sidenav';
import {MatListModule} from '@angular/material/list'; 
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTreeModule} from '@angular/material/tree';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HeaderComponent } from './header/header.component';
import { WorkspaceComponent } from './workspace/workspace.component';
import { ContactComponent } from './contact/contact.component';
import { HomepageComponent } from './homepage/homepage.component';
import { SignupComponent } from './signup/signup.component';
// import { SidenavComponent } from './sidenav/sidenav.component';
import { HttpClientModule } from '@angular/common/http';
import { ListComponent } from './list/list.component';
import { ClipboardModule } from '@angular/cdk/clipboard'
import { IvyCarouselModule } from 'angular-responsive-carousel'
import { TryComponent } from './try/try.component';
import {MatIconModule} from '@angular/material/icon';
import { JwtModule } from '@auth0/angular-jwt';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HeaderComponent,
    WorkspaceComponent,
    ContactComponent,
    HomepageComponent,
    SignupComponent,
    ListComponent,
    TryComponent,
  ],
  imports: [
    HttpClientModule,
    JwtModule.forRoot({
      config: {
        tokenGetter: () => {
          let token: string = localStorage.getItem("access_token");
          console.log("Sending token " + token);
          return localStorage.getItem("access_token");
        },
        allowedDomains: ["127.0.0.1:8000"],
        disallowedRoutes: ["http://127.0.0.1:8000/login/","http://127.0.0.1:8000/signup/"],
      }
    }),
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    MatToolbarModule,
    AceEditorModule,
    MatButtonModule,
    MatInputModule,
    MatCardModule,
    MatFormFieldModule,
    MatSidenavModule,
    MatListModule,
    MatTreeModule,
    ClipboardModule,
    IvyCarouselModule,
    MatIconModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
