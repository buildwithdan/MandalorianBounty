# MandalorianBounty
![visitors](https://visitor-badge.laobi.icu/badge?page_id=buildwithdan.MandalorianBounty)  
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/buildwithdan/MandalorianBounty)

A simple Flask Python CRUD app to understand how the basics of CRUD works with a database.   

# Stack

- **Framework**: [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- **Database**: [Supabase](https://supabase.com/)
- **Authentication**: not applicable
- **Deployment**: [Vercel](https://vercel.com)
- **Styling**: [Bootstrap](https://getbootstrap.com/)
- **Analytics**: not applicable


## To do:

- [x] need to fix the delete button
- [x] Add a create button for new contracts
- [x] Flash for add and delete
- [x] add vercel deploy
- [x] database variables to be kept outside of github (for now it uses a public DB created on supabase, so risk limited)

## Running Locally

This application requires the latest python and flask to be installed.

```bash
git clone https://github.com/buildwithdan/MandalorianBounty.git
cd MandalorianBounty
flask --debug --app api.app run
```

## Enviroment Variables
### Local
Ensure to plug your database details into the api/config.ini file.

### External
if you Deploy on Vervel, ensure to add your enviroment variables on the same naming as its in the config.ini file.

### config.py
have a look at the inside and just change the return value to local if you want to develop locally and then just flip it to external if you want it to work on Vercel.