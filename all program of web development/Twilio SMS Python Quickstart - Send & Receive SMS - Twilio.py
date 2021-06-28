<!DOCTYPE html>
<!-- saved from url=(0049)https://www.twilio.com/docs/sms/quickstart/python -->
<html class="no-js uk-notouch"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/elqCfg.min.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-pMn/at+iAgl0PpX8A+ccr7iPPScp0lIFsRTiC6EkDFtJ3fTeFBeJkP7nZJTcbD5h"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/mixpanel-2.2.min.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/munchkin.js.download"></script><script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/rules-p-efmoRQHrDUXig.js.download" async=""></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/dM4.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/6si.min.js.download"></script><script async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/clearbit.min.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/bf-munchkin.min.js.download"></script><script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/quant.js.download" async="" type="text/javascript"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/heap-1541905715.js.download"></script><script async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/uwt.js.download"></script><script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/1040773425961662" async=""></script><script async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/fbevents.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/hotjar-1359002.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/f.txt"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/insight.min.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/analytics.js.download"></script><script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/f.txt"></script><script async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/gtm.js.download"></script><script>
  var twilio = twilio || {};
  twilio.environment = "prod";
  twilio.baseUrl = "https://www.twilio.com";
  twilio.DOCSEARCH_APP_ID = "BH4D9OD16A";
  twilio.DOCSEARCH_API_KEY = "2dbc0c5e764a2669b21db8acc967fbd8";
  twilio.FACEBOOK_APP_ID = "414254592083321";


  twilio.account = twilio.account || {};
  
  twilio.account.sid = "AC53eb918d457ac68fb17d2273966afa35";
  

  twilio.user = twilio.user || {};
  
  twilio.user.sid = "USe9abe66b364abba79a19a822e0f4e6c6";
  
  
    twilio.user.visitorSid = "VI0fd35d2db6b4a9e40171f924f207d123";
  
  

  
  twilio.user.language = "php";
  

  

</script>

    <script>
  
    window.experiment = '';
  
</script>

    
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <meta name="viewport" content="width=device-width">
    
    
    <meta name="description" content="Learn how to send SMS text messages with Twilio&#39;s API and the Twilio Python helper library in this Programmable SMS Quickstart.">
    
    

    

    <title>
      Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio
    </title>

    
      <link rel="canonical" href="https://www.twilio.com/docs/sms/quickstart/python">
    

    
    
    <link rel="shortcut icon" href="https://www.twilio.com/docs/static/img/favicons/favicon.722f741d2.ico">
    <link rel="apple-touch-icon" href="https://www.twilio.com/docs/static/img/favicons/favicon_57.722f741d2.png">
    <link rel="apple-touch-icon" sizes="72x72" href="https://www.twilio.com/docs/static/img/favicons/favicon_72.722f741d2.png">
    <link rel="apple-touch-icon" sizes="114x114" href="https://www.twilio.com/docs/static/img/favicons/favicon_114.722f741d2.png">
    

    
    <link rel="stylesheet" href="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/fonts.min.722f741d2.css">
    <link rel="stylesheet" href="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/font-awesome.min.722f741d2.css">
    <link rel="stylesheet" href="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/devicon.min.722f741d2.css">
    <link rel="stylesheet" href="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/twilio-icons.722f741d2.css">

    
    <meta property="og:title" content="Twilio SMS Python Quickstart - Send &amp; Receive SMS">
    <meta property="og:description" content="Learn how to send SMS text messages with Twilio&#39;s API and the Twilio Python helper library in this Programmable SMS Quickstart.">
    
    <meta property="og:url" content="https://www.twilio.com/docs/sms/quickstart/python?utm_source=docs&amp;utm_medium=social&amp;utm_campaign=guides_tags">

    
    <meta property="twitter:title" content="Twilio SMS Python Quickstart - Send &amp; Receive SMS">
    <meta property="twitter:description" content="Learn how to send SMS text messages with Twilio&#39;s API and the Twilio Python helper library in this Programmable SMS Quickstart.">
    

    
    
    <meta property="fb:app_id" content="414254592083321">
    

    

    
      <link rel="stylesheet" href="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/docs.min.722f741d2.css">
    

    <!--  Stylesheet for docsearch -->
    <link rel="stylesheet" href="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/docsearch.min.css">

    
    
  <script type="text/javascript" async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/munchkin.js(1).download"></script><script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/f(1).txt"></script><script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/f(2).txt"></script><script async="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/modules.9b39a2b908035943c4d1.js.download" charset="utf-8"></script><style type="text/css">iframe#_hjRemoteVarsFrame {display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;}</style><style type="text/css">.txlive {display: none;}
</style><style type="text/css" id="qual_style-sy0"></style><style type="text/css" id="qual_style-sia"></style><script type="text/javascript" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/manifest.jsonp"></script></head>

  <body class="
    
      apireference
    
    
    
  ">

    

	
	<!-- Google Tag Manager -->
	<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-MWRD6S"
	height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
	<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
	new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
	j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
	'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
	})(window, document, 'script', 'dataLayer', 'GTM-MWRD6S');</script>
	<!-- End Google Tag Manager -->
	


    
    <div class="docs-banner">
        <div class="docs-seasonal-banner">
            
        </div>

        
        
        

<nav class="docs-nav docs-layout-nav">
  <div class="docs-nav__brand">
    
    <a href="https://www.twilio.com/docs" class="docs-nav__link router-link-exact-active router-link-active" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="logo"><span class="docs-nav__logo"><svg viewBox="0 0 30 30" xmlns="http://www.w3.org/2000/svg" class="twlo-logomark"><path fill="currentColor" d="M14.4,11.3c0,1.7-1.4,3.1-3.1,3.1S8.2,13,8.2,11.3s1.4-3.1,3.1-3.1S14.4,9.6,14.4,11.3z M11.3,15.6c-1.7,0-3.1,1.4-3.1,3.1 s1.4,3.1,3.1,3.1s3.1-1.4,3.1-3.1S13,15.6,11.3,15.6z M30,15c0,8.3-6.7,15-15,15S0,23.3,0,15S6.7,0,15,0S30,6.7,30,15z M26,15 c0-6.1-4.9-11-11-11S4,8.9,4,15s4.9,11,11,11S26,21.1,26,15z M18.7,15.6c-1.7,0-3.1,1.4-3.1,3.1s1.4,3.1,3.1,3.1s3.1-1.4,3.1-3.1 S20.4,15.6,18.7,15.6z M18.7,8.2c-1.7,0-3.1,1.4-3.1,3.1s1.4,3.1,3.1,3.1s3.1-1.4,3.1-3.1S20.4,8.2,18.7,8.2z"></path></svg></span> <span class="docs-nav__title">Twilio Docs</span></a>
    
  </div>

  <ul class="docs-nav__primary">
    
    <li class="docs-nav__item">
      
        <a href="https://www.twilio.com/docs/sms" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="SMS">SMS</a>
      
    </li>
    
    <li class="docs-nav__item">
      
        <a href="https://www.twilio.com/docs/voice" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Voice">Voice</a>
      
    </li>
    
    <li class="docs-nav__item">
      
        <a href="https://www.twilio.com/docs/runtime" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Runtime">Runtime</a>
      
    </li>
    
    <li class="docs-nav__item">
      
        <a href="https://www.twilio.com/docs/video" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Video">Video</a>
      
    </li>
    
    <li class="docs-nav__item">
      
        <a href="https://www.twilio.com/docs/studio" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Studio">Studio</a>
      
    </li>
    
    <li class="docs-nav__item">
      
        <a href="https://www.twilio.com/docs/all" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="All docs...">All docs...</a>
      
    </li>
    
  </ul>

  <ul class="docs-nav__secondary">
    
    <li class="docs-nav__item">
      
        <a href="https://www.twilio.com/docs/libraries" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="SDKs">SDKs</a>
      
    </li>
    
    <li class="docs-nav__item">
      
        <a href="https://support.twilio.com/hc/en-us" target="_blank" class="docs-nav__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Help">Help</a>
      
    </li>
    
    <li class="docs-nav__docsearch">
      <span class="algolia-autocomplete" style="position: relative; display: inline-block; direction: ltr;"><input type="search" name="q" placeholder="Search" id="docsearch" class="ds-input" autocomplete="off" spellcheck="false" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-label="search input" aria-owns="algolia-autocomplete-listbox-0" dir="auto" style="position: relative; vertical-align: top;"><pre aria-hidden="true" style="position: absolute; visibility: hidden; white-space: pre; font-family: &quot;Whitney SSm A&quot;, &quot;Whitney SSm B&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 15px; font-style: normal; font-variant: normal; font-weight: 400; word-spacing: 0px; letter-spacing: normal; text-indent: 0px; text-rendering: auto; text-transform: none;"></pre><span class="ds-dropdown-menu" role="listbox" id="algolia-autocomplete-listbox-0" style="position: absolute; top: 100%; z-index: 100; display: none; left: 0px; right: auto;"><div class="ds-dataset-1"></div></span></span>
    </li>

    
    
      <li class="docs-nav__item">
        <a href="https://www.twilio.com/console" class="docs-nav__console" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="console">
          <svg class="twlo-icon-interface-user" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path fill="currentColor" d="M5 5c0-1.7 1.3-3 3-3s3 1.3 3 3-1.3 3-3 3-3-1.3-3-3zm3 5c-3.3 0-6 2.7-6 6h12c0-3.3-2.7-6-6-6z"></path></svg>
          Console
        </a>
      </li>
    
    
  </ul>

  <span class="docs-nav-mobile">
      <div class="docs-navicon">
          <a href="https://www.twilio.com/docs/sms/quickstart/python#" class="docs-navicon__trigger">
              <div class="docs-navicon__lines">
                  <span class="docs-navicon__lines--center"></span>
              </div>
          </a>
      </div>
      <ul class="docs-nav-mobile__menu">
          <li><form method="get" action="https://www.twilio.com/docs/search"><input type="search" name="q" class="docs-nav-mobile__search"></form></li>

      
        
          <li><a href="https://www.twilio.com/docs/sms" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="SMS">SMS</a></li>
        
      
        
          <li><a href="https://www.twilio.com/docs/voice" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Voice">Voice</a></li>
        
      
        
          <li><a href="https://www.twilio.com/docs/runtime" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Runtime">Runtime</a></li>
        
      
        
          <li><a href="https://www.twilio.com/docs/video" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Video">Video</a></li>
        
      
        
          <li><a href="https://www.twilio.com/docs/studio" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Studio">Studio</a></li>
        
      
        
          <li><a href="https://www.twilio.com/docs/all" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="All docs...">All docs...</a></li>
        
      

      
        
          <li><a href="https://www.twilio.com/docs/libraries" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="SDKs">SDKs</a></li>
        
      
        
          <li><a href="https://support.twilio.com/hc/en-us" target="_blank" class="docs-nav-mobile__link" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="Help">Help</a></li>
        
      
      
          <li><a href="https://www.twilio.com/login" class="docs-nav-mobile__login" data-glinktype="site navigation" data-glinklocation="docs" data-glinkname="log in">Log in</a></li>
          <li><a href="https://www.twilio.com/try-twilio" class="docs-nav-mobile__signup" data-glinktype="cta-link" data-glinklocation="docs" data-glinkname="signup-sign-up">Sign up</a></li>
      
      </ul>
  </span>
</nav>

        
    </div>
    



<div class="docs-layout" style="margin-top: 50px; height: 559px;">
<div class="docs-sidebar docs-layout-sidebar">
<div class="docs-sidebar__header">
<a class="docs-sidebar__title router-link-exact-active router-link-active" href="https://www.twilio.com/docs/sms">
        Programmable SMS
      </a>
<a class="docs-sidebar__status" href="https://status.twilio.com/" id="twilio-status-link" target="_blank" twilio_status_url="/docs/twilio_status/twilio/s2k3h0mkqnth">
<div class="docs-sidebar__status-indicator"></div>
<div class="docs-sidebar__status-overlay">
<p class="docs-sidebar__status-title">PROGRAMMABLE MESSAGING</p>
<p class="docs-sidebar__status-subtitle">Operational</p>
</div>
</a>
</div>
<div class="docs-sidebar__mobile-menu">
<p class="docs-sidebar__mobile-menu-title">Menu</p>
<svg class="twlo-icon-interface-dropdown" height="18" viewBox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg">
<path d="M15 7l-6 6-6-6V6h1l5 5 5-5h1v1z" fill="currentColor"></path>
</svg>
</div>
<div class="docs-sidebar__content">
<ul class="docs-sidebar__file-tree">
<!-- Page menu entries -->
<li class="folder">
<input checked="" id="getting-started" name="getting-started" type="checkbox">
<label for="getting-started">Getting Started</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="page">
<a href="https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account">
          How to Work with your Free Twilio Trial Account
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/quickstart/php">
          PHP Quickstart
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/quickstart/csharp-dotnet-framework">
          .NET Framework Quickstart
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/quickstart/csharp-dotnet-core">
          .NET Core Quickstart
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/quickstart/java">
          Java Quickstart
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/quickstart/node">
          Node.js Quickstart
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/quickstart/ruby">
          Ruby Quickstart
      </a>
</li>
<li class="page is-selected">
<a href="https://www.twilio.com/docs/sms/quickstart/python">
          Python Quickstart
      </a>
</li>
<ul class="menu-accordion expanded" id="doc-navigation" role="menu-accordion" style="display: block;"><li class="hash" id="doc-nav-0"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#sign-up-for-or-sign-in-to-twilio">Sign up for - or sign in to - Twilio</a></li><li class="hash" id="doc-nav-1"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#install-the-twilio-cli">Install the Twilio CLI</a></li><li class="hash" id="doc-nav-2"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#get-a-phone-number">Get a phone number</a></li><li class="hash" id="doc-nav-3"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#install-python-and-the-twilio-helper-library">Install Python and the Twilio Helper Library</a></li><li class="hash" id="doc-nav-4"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#send-an-outbound-sms-with-python">Send an outbound SMS with Python</a></li><li class="hash" id="doc-nav-5"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#set-up-a-twilio-messaging-service">Set up a Twilio Messaging Service</a></li><li class="hash" id="doc-nav-6"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#create-a-messaging-service-with-your-phone-number">Create a Messaging Service with your phone number</a></li><li class="hash" id="doc-nav-7"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#send-an-sms-from-your-messaging-service">Send an SMS from your Messaging Service</a></li><li class="hash" id="doc-nav-8"><a class="intrapage" href="https://www.twilio.com/docs/sms/quickstart/python#where-to-next">Where to next?</a></li></ul>
</ul>
</li>
<li class="folder">
<input checked="" id="api-reference" name="api-reference" type="checkbox">
<label for="api-reference">API Reference</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="page">
<a href="https://www.twilio.com/docs/sms/api">
          API Overview
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/api/message-resource">
          Message Resource
      </a>
</li>
<ul class="menu-accordion expanded child-subsection">
<li class="page">
<a href="https://www.twilio.com/docs/sms/api/message-feedback-resource">
          MessageFeedback Resource
      </a>
</li>
</ul>
<li class="page">
<a href="https://www.twilio.com/docs/sms/api/media-resource">
          Media Resource
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/messaging/services/api">
          Service Resource
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/api/pricing">
          Pricing
      </a>
</li>
</ul>
</li>
<li class="folder">
<input checked="" id="twiml" name="twiml" type="checkbox">
<label for="twiml">TwiML</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="page">
<a href="https://www.twilio.com/docs/sms/twiml">
          Overview
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/twiml/message">
          &lt;Message&gt;
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/twiml/redirect">
          &lt;Redirect&gt;
      </a>
</li>
</ul>
</li>
<li class="folder">
<input checked="" id="tutorials" name="tutorials" type="checkbox">
<label for="tutorials">Tutorials</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="page">
<a href="https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply">
          How to receive and reply to SMS messages
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/tutorials/server-notifications">
          Build Server Notifications with SMS
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages">
          How to send SMS and MMS messages
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/tutorials/how-to-confirm-delivery">
          How to track delivery status of messages
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/tutorials/appointment-reminders">
          Appointment Reminders
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/tutorials/how-to-retrieve-and-modify-message-history">
          How to retrieve and modify message history
      </a>
</li>
<li class="code">
<a href="https://www.twilio.com/docs/tutorials?filter-product=sms">
        Browse all SMS tutorials
    </a>
</li>
</ul>
</li>
<li class="folder">
<input checked="" id="programmable-sms-usage-guides" name="programmable-sms-usage-guides" type="checkbox">
<label for="programmable-sms-usage-guides">Programmable SMS usage guides</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="page">
<a href="https://www.twilio.com/docs/sms/send-messages">
          Send messages with the API
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/send-message-feedback-to-twilio">
          Send message feedback to Twilio
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/app-verification">
          App verification with Twilio SMS
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/tutorials/sending-international-sms-guide">
          What to Know Before Sending International SMS Messages
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/migrate">
          Migrate to Twilio
      </a>
</li>
</ul>
</li>
<li class="folder">
<input checked="" id="a2p-10dlc" name="a2p-10dlc" type="checkbox">
<label for="a2p-10dlc">A2P 10DLC</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="page">
<a href="https://www.twilio.com/docs/sms/a2p-10dlc/onboarding">
          Direct Brand Onboarding Guide
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/a2p-10dlc/onboarding-isv">
          ISV Onboarding Guide
      </a>
</li>
</ul>
</li>
<li class="folder">
<input checked="" id="troubleshooting" name="troubleshooting" type="checkbox">
<label for="troubleshooting">Troubleshooting</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="page">
<a href="https://www.twilio.com/docs/sms/debugging-tools">
          Twilio's Debugging Tools
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/debugging-common-issues">
          Debugging Common SMS Issues
      </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/sms/accepted-mime-types">
          Accepted Content Types for Media
      </a>
</li>
<li class="code">
<a href="https://twiliodeved.github.io/message-segment-calculator/">
        Messaging Segment Calculator
    </a>
</li>
</ul>
</li>
<li class="folder">
<input checked="" id="programmable-messaging" name="programmable-messaging" type="checkbox">
<label for="programmable-messaging">Programmable Messaging</label>
<ul class="menu-accordion" role="menu-accordion">
<li class="code">
<a href="https://www.twilio.com/docs/messaging">
        All Programmable Messaging Docs
    </a>
</li>
<li class="code">
<a href="https://www.twilio.com/docs/messaging/services">
        Messaging Service Features
    </a>
</li>
<li class="code">
<a href="https://www.twilio.com/docs/messaging/services/api">
        API Reference: Messaging Services
    </a>
</li>
<li class="code">
<a href="https://www.twilio.com/docs/messaging/channels">
        Twilio Messaging Channels
    </a>
</li>
<li class="page">
<a href="https://www.twilio.com/docs/messaging/guides/webhook-request">
          Twilio's Request to your Webhook URL
      </a>
</li>
<li class="code">
<a href="https://www.twilio.com/docs/whatsapp">
        Looking for the WhatsApp Business API with Twilio?
    </a>
</li>
<li class="code">
<a href="https://www.twilio.com/docs/conversations">
        Twilio Conversations for two-way messaging
    </a>
</li>
</ul>
</li>
</ul>
</div>
</div>
<main class="docs-layout-main docs-layout-multi-columns" style="height: 559px;">
<div class="docs-layout-column" style="height: 559px;">
<div class="docs-reader-mode-toggle">
<span class="docs-reader-mode-toggle__label hidden">Collapse</span>
<svg class="icon-minimize hidden" height="18" viewBox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M4 0h2v6H0V4h4V0zm0 18v-4H0v-2h6v6H4zm14-4h-4v4h-2v-6h6v2zM14 0v4h4v2h-6V0h2z" fill="#FFF" fill-rule="nonzero"></path></svg>
<span class="docs-reader-mode-toggle__label">Expand</span>
<svg class="icon-maximize" height="18" viewBox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M2 6H0V0h6v2H2v4zm0 6v4h4v2H0v-6h2zm10 4h4v-4h2v6h-6v-2zm4-10V2h-4V0h6v6h-2z" fill="#FFF" fill-rule="nonzero"></path></svg>
</div>
<div class="rating-wrapper">
<div class="rating-stars" data-rating="0">
<span class="rating-label">Rate this page:</span>
<ol><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li></ol></div>
</div>
<article class="docs-article docs-prose">
<header>
<h1 class="docs-article__title">
        Twilio SMS Python Quickstart
      </h1>
</header>
<section>
<p>With just a few lines of code, your Python application can send SMS messages with <a href="https://www.twilio.com/docs/sms">Twilio Programmable Messaging</a>.</p>
<p>This Programmable Messaging Quickstart will walk you through the entire process step-by-step, starting with setting up your Twilio account all the way through sending an SMS using a Messaging Service.</p>
<p>In this Quickstart, you will learn how to:</p>
<ul class="docs-article__list">
<li>Sign up for Twilio and get your first SMS-enabled Twilio phone number</li>
<li>Set up your development environment to send outbound messages</li>
<li>Send your first outbound SMS</li>
<li>Set up your first Twilio Messaging Service</li>
<li>Send a second SMS from that Messaging Service</li>
</ul>
<p>By the end of this Quickstart, you’ll have a solid foundation for building and scaling with Twilio’s Programmable Messaging for your specific use cases.</p>
</section>
<section class="docs-article__next_step">
<a class="twlo-btn cursor-hover pulse" href="https://www.twilio.com/docs/sms/quickstart/python#">
  Show me how it's done!
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="sign-up-for-or-sign-in-to-twilio"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#sign-up-for-or-sign-in-to-twilio">Sign up for - or sign in to - Twilio</a></h2>
</section>
<section class="is-hidden">
<div class="docs-note docs-note--info">
<p>Already have a Twilio account? Go ahead and <a href="https://www.twilio.com/docs/sms/quickstart/python#install-the-twilio-cli">skip this section</a>.</p>
</div>
</section>
<section class="is-hidden">
<div class="block-rich_text">
<p>You can sign up for a free Twilio trial account <a href="https://www.twilio.com/try-twilio">here</a>.</p>
<ul class="docs-article__list">
<li>When you sign up, you'll be asked to verify your personal phone number. This helps Twilio verify your identity and also allows you to send test messages to your phone from your Twilio account while in trial mode.</li>
<li>Once you verify your number, you'll be asked a series of questions to customize your experience.</li>
<li>Once you finish the onboarding flow, you'll arrive at your project dashboard in the <a href="https://www.twilio.com/console">Twilio Console</a>. This is where you'll be able to access your Account SID, authentication token, find a Twilio phone number, and more.</li>
</ul>
</div>
</section>
<section class="docs-article__next_step is-hidden">
<a class="twlo-btn cursor-hover" href="https://www.twilio.com/docs/sms/quickstart/python#">
  I've got an account! What's next?
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="install-the-twilio-cli"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#install-the-twilio-cli">Install the Twilio CLI</a></h2>
<p>We'll use the Twilio CLI (command line interface) for a few tasks, so let's install that next.</p>
</section>
<section class="is-hidden">
<div class="block-tabbed_content">
<div class="docs-tabs__buttons">
<button class="docs-tabs__button active" data-tab-group-id="macos|windows|linux" data-tab-id="macos" id="macos-1">
      macOS
    </button>
<button class="docs-tabs__button" data-tab-group-id="macos|windows|linux" data-tab-id="windows" id="windows-1">
      Windows
    </button>
<button class="docs-tabs__button" data-tab-group-id="macos|windows|linux" data-tab-id="linux" id="linux-1">
      Linux
    </button>
</div>
<section class="docs-tabs__content active" data-tab-group-id="macos|windows|linux" data-tab-id="macos">
<p>One of the easiest ways to install the CLI on macOS is to use <a href="https://brew.sh/">Homebrew</a>. If you don't already have it installed, <a href="https://brew.sh/">visit the Homebrew site</a> for installation instructions and then return here.</p>
<p>Once Homebrew is installed, simply run the following command to install the CLI:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">brew tap twilio/brew &amp;&amp; brew install twilio
</span></pre></div>
<h4 class="docs-article__section-title" id="updating-1"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#updating-1">Updating</a></h4>
<p>If you already installed the CLI with brew and want to upgrade to the latest version, run:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">brew upgrade twilio
</span></pre></div>
<h4 class="docs-article__section-title" id="warning-for-nodejs-developers"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#warning-for-nodejs-developers">Warning for Node.js developers</a></h4>
<p>If you have installed Node.js version 10.12 or higher on your Mac, you can avoid potential Node.js version conflicts by installing the CLI using npm:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">npm install twilio-cli -g
</span></pre></div>
</section>
<section class="docs-tabs__content" data-tab-group-id="macos|windows|linux" data-tab-id="windows">
<p>Before we can install, we need to make sure you have <a href="https://nodejs.org/">Node.js</a> installed (version 10.12 or above). To see if you have node installed, try running this command:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">node -v
</span></pre></div>
<p>If your system reports v10.12.0 or above, you can skip the next step.</p>
<h4 class="docs-article__section-title" id="installing-nodejs-on-windows"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#installing-nodejs-on-windows">Installing Node.js on Windows</a></h4>
<p>Using the Windows Installer (.msi) is the recommended way to install Node.js on Windows. You can download the installer from <a href="https://nodejs.org/en/download/">the Node.js download page</a>.</p>
<h4 class="docs-article__section-title" id="installing-twilio-cli-1"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#installing-twilio-cli-1">Installing Twilio CLI</a></h4>
<p>The CLI is installed with <a href="https://www.npmjs.com/">npm</a> (Node Package Manager), which comes with Node.js. To install the CLI run the following command:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">npm install twilio-cli -g
</span></pre></div>
<p>Note the -g option is what installs the command globally so you can run it from anywhere in your system.</p>
<h4 class="docs-article__section-title" id="updating-2"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#updating-2">Updating</a></h4>
<p>If you already installed the CLI with npm and want to upgrade to the latest version, run:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">npm install twilio-cli@latest -g
</span></pre></div>
</section>
<section class="docs-tabs__content" data-tab-group-id="macos|windows|linux" data-tab-id="linux">
<p>Before we can install, we need to make sure you have Node.js installed (version 10.12 or above). Even if you already installed Node yourself, the CLI works best when you install it using nvm. Here's how to get nvm installed on most Linux systems:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
</span></pre></div>
<p>Please visit the <a href="https://github.com/nvm-sh/nvm#installation-and-update">nvm installation instructions</a> for additional options and troubleshooting steps. Once you have nvm installed, run the following to install and use the most recent LTS release of Node.js:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">nvm install --lts
</span><span class="code-line">nvm use &lt;insert version reported from above&gt;
</span></pre></div>
<h4 class="docs-article__section-title" id="installing-other-twilio-cli-prerequisites-for-linux"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#installing-other-twilio-cli-prerequisites-for-linux">Installing other Twilio CLI prerequisites for Linux</a></h4>
<p>Depending on your distribution, you will need to run one of the following commands:</p>
<ul class="docs-article__list">
<li>Debian/Ubuntu: <code>sudo apt-get install libsecret-1-dev</code></li>
<li>Red Hat-based: <code>sudo yum install libsecret-devel</code></li>
<li>Arch Linux: <code>sudo pacman -S libsecret</code></li>
</ul>
<h4 class="docs-article__section-title" id="installing-twilio-cli-2"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#installing-twilio-cli-2">Installing Twilio CLI</a></h4>
<p>The CLI is installed with <a href="https://www.npmjs.com/">npm</a> (Node Package Manager), which comes with Node.js. To install the CLI run the following command:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">npm install twilio-cli -g
</span></pre></div>
<p>Note the -g option is what installs the command globally so you can run it from anywhere in your system.</p>
<h4 class="docs-article__section-title" id="updating-3"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#updating-3">Updating</a></h4>
<p>If you already installed the CLI with npm and want to upgrade to the latest version, run:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">npm install twilio-cli@latest -g
</span></pre></div>
</section>
</div>
</section>
<section class="is-hidden">
<p>Run <code>twilio login</code> to get the Twilio CLI connected to your account. Visit <a href="https://www.twilio.com/console">https://www.twilio.com/console</a>, and you’ll find your unique Account SID and Auth Token to provide to the CLI.</p>
<p>You can reveal your auth token by clicking on the eyeball icon:</p>
<p></p><figure class="figure-richtext-image figure-full-width"><div class="lightbox-img-wrapper"><a class="lightbox-img-anchor"><img alt="Reveal Your Auth Token" class="richtext-image full-width" height="117" sizes="463px" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/account_sid_auth_token.width-800.png" srcset="https://twilio-cms-prod.s3.amazonaws.com/images/account_sid_auth_token.width-800.png 463w, https://twilio-cms-prod.s3.amazonaws.com/images/account_sid_auth_token.width-1600.png 463w" width="463"><div class="lightbox-img-wrapper-overlay"><i class="fa fa-search-plus" aria-hidden="true"></i></div></a></div><div class="docs-modal-overlay" style="display: none;"><div class="docs-modal"><span class="docs-modal__close">
<svg class="icon-close" fill="#233659" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4l-5 5 5 5v1h-1l-5-5-5 5H3v-1l5-5-5-5V3h1l5 5 5-5h1v1z"></path></svg></span><img alt="Reveal Your Auth Token" class="richtext-image full-width" height="117" sizes="463px" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/account_sid_auth_token.width-800.png" srcset="https://twilio-cms-prod.s3.amazonaws.com/images/account_sid_auth_token.width-800.png 463w, https://twilio-cms-prod.s3.amazonaws.com/images/account_sid_auth_token.width-1600.png 463w" width="463"></div></div></figure><p></p>
</section>
<section class="docs-article__next_step is-hidden">
<a class="twlo-btn cursor-hover" href="https://www.twilio.com/docs/sms/quickstart/python#">
  Now to get a phone number...
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="get-a-phone-number"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#get-a-phone-number">Get a phone number</a></h2>
<p>If you don't currently own a Twilio phone number with SMS functionality, you'll need to purchase one. With the CLI, run:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">twilio phone-numbers:buy:local --country-code US --sms-enabled
</span></pre></div>
</section>
<section class="is-hidden">
<div class="docs-note docs-note--info">
<p>Replace <strong>US</strong> with your <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO-3166-1 country code</a> if you would like a phone number in another country. If you aren't finding any SMS enabled numbers, try looking for a mobile number instead of a local number: <code>twilio phone-numbers:buy:mobile --country-code DE --sms-enabled</code></p>
</div>
</section>
<section class="is-hidden">
<p>Select a phone number to add it to your account.</p>
<p>Next, we need to install Python and the Twilio Python Helper Library.</p>
</section>
<section class="docs-article__next_step is-hidden">
<a class="twlo-btn cursor-hover" href="https://www.twilio.com/docs/sms/quickstart/python#">
  No problem! Take me through the setup.
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="install-python-and-the-twilio-helper-library"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#install-python-and-the-twilio-helper-library">Install Python and the Twilio Helper Library</a></h2>
</section>
<section class="is-hidden">
<div class="docs-note docs-note--info">
<p>If you’ve gone through one of our other Python Quickstarts already and have Python and the Twilio Python helper library installed, you can skip this step and <a href="https://www.twilio.com/docs/sms/quickstart/python#send-an-outbound-sms-with-python">get straight to sending your first text message</a>.</p>
</div>
</section>
<section class="is-hidden">
<p>To send your first SMS, you’ll need to have Python and the Twilio Python helper library installed.</p>
</section>
<section class="is-hidden">
<div class="block-rich_text">
<h4 class="docs-article__section-title" id="install-python"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#install-python">Install Python</a></h4>
<p>If you’re using a Mac or Linux machine, you probably already have Python installed. You can check this by opening up a terminal and running the following command:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">python --version
</span></pre></div>
<p>You should see something like:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">$ python --version
</span><span class="code-line">Python 3.4
</span></pre></div>
<p>Windows users can follow this <a href="https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10">excellent tutorial for installing Python on Windows</a>, or follow the <a href="https://docs.python.org/3/using/windows.html">instructions from Python's documentation</a>.</p>
<p>Twilio’s Python server-side SDK supports both Python 2 and Python 3. You can use either version for this quickstart, but we recommend using Python 3 for future projects with Twilio unless there are specific libraries your project needs which are only compatible with Python 2.</p>
<p> </p>
<h4 class="docs-article__section-title" id="install-the-twilio-python-server-side-sdk"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#install-the-twilio-python-server-side-sdk">Install the Twilio Python Server-side SDK</a></h4>
<p>The easiest way to install the library is using <a href="http://www.pip-installer.org/en/latest/">pip</a>, a package manager for Python that makes it easier to install the libraries you need. Simply run this in the terminal:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">pip install twilio
</span></pre></div>
<p>If you get a <code>pip: command not found</code> error, you can also use <code>easy_install</code> by running this in your terminal:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">easy_install twilio
</span></pre></div>
<p>If you'd prefer a manual installation, you can <a href="https://github.com/twilio/twilio-python/zipball/master">download the source code (ZIP)</a> for <code>twilio-python</code> and then install the library by running:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">python setup.py install
</span></pre></div>
<p>in the folder containing the twilio-python server-side SDK library code.</p>
</div>
</section>
<section class="docs-article__next_step is-hidden">
<a class="twlo-btn cursor-hover" href="https://www.twilio.com/docs/sms/quickstart/python#">
  All set! Let's send a text message.
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="send-an-outbound-sms-with-python"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#send-an-outbound-sms-with-python">Send an outbound SMS with Python</a></h2>
<p>Now that we have Python and <code>twilio-python</code> installed, we can send an outbound text message from the Twilio phone number we just purchased with a single API request. Create and open a new file called <code>send_sms.py</code> and type or paste in this code sample.</p>
</section>
<section class="is-hidden">
<div class="code-sample" data-title="Send an SMS Using Twilio" id="code-send-an-sms-using-twilio">
<div class="inline-mode">
<div class="twlo-code code-rail" id="coderail">
<div class="rail-placeholder"></div>
<header class="twlo-code-header rail-title">
<div class="twlo-code-header__title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#linkcode">
<div class="twlo-code-header__title-inner">Send an SMS Using Twilio</div>
<div class="twlo-code-header__title-loading"></div>
</a>
</div>
<ul class="twlo-code-header__dropdown"></ul>
<div class="twlo-code-header__actions">
<ul class="twlo-code-header__languages"><li class="twlo-code-header__language is-selected" data-sample-language="Python">Python</li></ul>
<ul class="twlo-code-header__versions"><li class="twlo-code-header__version is-selected">6.x</li></ul>
</div>
</header>
<div class="twlo-code__sample">
<div class="twlo-code__actions">
<span class="twlo-code__action twlo-code__outdated" style="display: none;">
        You are viewing an outdated version of this SDK.
      </span>
<span class="twlo-code__action clippy">
<svg class="twlo-icon-interface-clipboard" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M16 7v2h-5v2L8 8l3-3v2h5zM8 5H4v1h4V5zm-4 7h5v-1H4v1zm9-1h1v3H2V0h12v5h-1V3H3v10h10v-2zM3 2h10V1H3v1zm1 7v1h3V9H4zm0-1h3V7H4v1z" fill="currentColor"></path></svg>
</span>
<a class="twlo-code__action github hidden" href="https://github.com/" target="_blank">
<svg class="twlo-icon-interface-repo" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M5 3H4V2h1v1zm0 1H4v1h1V4zm0 4H4v1h1V8zm0-2H4v1h1V6zm9-6v14H7v2l-1.5-1L4 16v-2H2V0h12zm-1 11H3v2h1v-1h3v1h6v-2zm0-10H3v9h10V1z" fill="currentColor"></path></svg>
</a>
</div>
<pre class="twlo-code__snippet line-numbers"><code class="codehilite notranslate language-py"><span class="code-line"><span class="c1"># Download the helper library from https://www.twilio.com/docs/python/install</span><br></span><span class="code-line"><span class="kn">import</span> <span class="nn">os</span><br></span><span class="code-line"><span class="kn">from</span> <span class="nn">twilio.rest</span> <span class="kn">import</span> <span class="n">Client</span><br></span><span class="code-line"><br></span><span class="code-line"><br></span><span class="code-line"><span class="c1"># Your Account Sid and Auth Token from twilio.com/console</span><br></span><span class="code-line"><span class="c1"># and set the environment variables. See http://twil.io/secure</span><br></span><span class="code-line"><span class="n">account_sid</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s1">'TWILIO_ACCOUNT_SID'</span><span class="p">]</span><br></span><span class="code-line"><span class="n">auth_token</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s1">'TWILIO_AUTH_TOKEN'</span><span class="p">]</span><br></span><span class="code-line"><span class="n">client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="n">account_sid</span><span class="p">,</span> <span class="n">auth_token</span><span class="p">)</span><br></span><span class="code-line"><br></span><span class="code-line"><span class="n">message</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">messages</span> \<br></span><span class="code-line">                <span class="o">.</span><span class="n">create</span><span class="p">(</span><br></span><span class="code-line">                     <span class="n">body</span><span class="o">=</span><span class="s2">"Join Earth's mightiest heroes. Like Kevin Bacon."</span><span class="p">,</span><br></span><span class="code-line">                     <span class="n">from_</span><span class="o">=</span><span class="s1">'+15017122661'</span><span class="p">,</span><br></span><span class="code-line">                     <span class="n">to</span><span class="o">=</span><span class="s1">'+15558675310'</span><br></span><span class="code-line">                 <span class="p">)</span><br></span><span class="code-line"><br></span><span class="code-line"><span class="nb">print</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">sid</span><span class="p">)</span><br></span><span class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<div class="docs-coderail__next" style="display: none;">
<a class="docs-coderail__next-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Next Sample</a>
</div>
<div class="docs-coderail__show_output">
<a class="docs-coderail__show_output-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Show sample response</a>
</div>
</div>
<div class="twlo-code__output" style="display: none;">
<div class="docs-coderail__label">Example JSON API response</div>
<pre class="twlo-code__snippet line-numbers language-json"></pre>
</div>
<div class="twlo-code__info" data-id="code-send-an-sms-using-twilio"></div>
<script>
//<sl:notranslate>
codeRails = window.twilio.codeRails || {};

codeRails["code-send-an-sms-using-twilio"] = {
  title: "Send an SMS Using Twilio",
  sampleType: "server",
  downloadUrl: "",
  githubUrl: "",
  id: "",
  htmlId: "code-send-an-sms-using-twilio",
  samples: [
    
    {
      "extension": "py",
      "language": "Python",
      "version": "6.x",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;c1&quot;&gt;# Download the helper library from https://www.twilio.com/docs/python/install&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;kn&quot;&gt;import&lt;/span&gt; &lt;span class=&quot;nn&quot;&gt;os&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;kn&quot;&gt;from&lt;/span&gt; &lt;span class=&quot;nn&quot;&gt;twilio.rest&lt;/span&gt; &lt;span class=&quot;kn&quot;&gt;import&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;Client&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;c1&quot;&gt;# Your Account Sid and Auth Token from twilio.com/console&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;c1&quot;&gt;# and set the environment variables. See http://twil.io/secure&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;account_sid&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;os&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;environ&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;[&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;TWILIO_ACCOUNT_SID&amp;#39;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;]&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;auth_token&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;os&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;environ&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;[&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;TWILIO_AUTH_TOKEN&amp;#39;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;]&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;client&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;Client&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;(&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;account_sid&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;auth_token&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;)&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;message&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;client&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;messages&lt;/span&gt; \\&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;                &lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;create&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;(&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;                     &lt;span class=&quot;n&quot;&gt;body&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;=&lt;/span&gt;&lt;span class=&quot;s2&quot;&gt;&amp;quot;Join Earth&amp;#39;s mightiest heroes. Like Kevin Bacon.&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;                     &lt;span class=&quot;n&quot;&gt;from_&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;=&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;+15017122661&amp;#39;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;                     &lt;span class=&quot;n&quot;&gt;to&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;=&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;+15558675310&amp;#39;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;                 &lt;span class=&quot;p&quot;&gt;)&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;nb&quot;&gt;print&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;(&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;message&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;sid&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;)&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ],
  outputs: [
    
    {
      "extension": "json",
      "language": "JSON",
      "version": "",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;account_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;api_version&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;2010-04-01&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;body&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Join Earth&amp;#39;s mightiest heroes. Like Kevin Bacon.&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_created&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:31 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_updated&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;direction&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;outbound-api&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_code&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_message&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;from&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+15017122661&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;messaging_service_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;0&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_segments&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;1&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price_unit&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;status&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;subresource_uris&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;nt&quot;&gt;&amp;quot;media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;p&quot;&gt;},&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;to&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+15558675310&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;uri&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;}&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ]
};

window.twilio.codeRails = codeRails;
//</sl:notranslate>
</script>
</div>
<div class="rail-caption">
      This code creates a new instance of the Message resource and sends an HTTP POST to the Message resource URI.
    </div>
</div>
<div class="button-mode">
<div class="docs-article__code-cta cursor-hover">
<div class="docs-article__code-cta-cursor-wrap">
<div class="docs-article__code-cta-cursor"></div>
</div>
<div class="docs-article__code-cta-body">
<h4 class="docs-article__code-cta-title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#">Send an SMS Using Twilio</a>
</h4>
<div class="docs-article__code-cta-path">This code creates a new instance of the Message resource and sends an HTTP POST to the Message resource URI.</div>
</div>
<div class="docs-article__code-cta-arrow"></div>
</div>
</div>
</div>
</section>
<section class="is-hidden">
<p>You’ll need to edit your send_sms.py file a little more before your message will send:</p>
<h4 class="docs-article__section-title" id="replace-the-placeholder-credential-values"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#replace-the-placeholder-credential-values">Replace the placeholder credential values</a></h4>
<p>Swap the placeholder values for <code>account_sid</code> and <code>auth_token</code> with your personal Twilio credentials. Go to <a href="https://www.twilio.com/console">https://www.twilio.com/console</a> and log in. On this page, you’ll find your unique Account SID and Auth Token, which you’ll need any time you send messages through the Twilio Client like this. You can reveal your auth token by clicking on the 'view' link:</p>
<p></p><figure class="figure-richtext-image figure-full-width"><div class="lightbox-img-wrapper"><a class="lightbox-img-anchor"><img alt="Reveal your Auth Token in the Twilio Console" class="richtext-image full-width" height="106" sizes="584px" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/console-project-auth-token.width-800.png" srcset="https://twilio-cms-prod.s3.amazonaws.com/images/console-project-auth-token.width-800.png 584w, https://twilio-cms-prod.s3.amazonaws.com/images/console-project-auth-token.width-1600.png 584w" width="584"><div class="lightbox-img-wrapper-overlay"><i class="fa fa-search-plus" aria-hidden="true"></i></div></a></div><div class="docs-modal-overlay" style="display: none;"><div class="docs-modal"><span class="docs-modal__close">
<svg class="icon-close" fill="#233659" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18"><path d="M15 4l-5 5 5 5v1h-1l-5-5-5 5H3v-1l5-5-5-5V3h1l5 5 5-5h1v1z"></path></svg></span><img alt="Reveal your Auth Token in the Twilio Console" class="richtext-image full-width" height="106" sizes="584px" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/console-project-auth-token.width-800.png" srcset="https://twilio-cms-prod.s3.amazonaws.com/images/console-project-auth-token.width-800.png 584w, https://twilio-cms-prod.s3.amazonaws.com/images/console-project-auth-token.width-1600.png 584w" width="584"></div></div></figure><p></p>
<p> Open <code>send_sms.py</code> and replace the values for <code>account_sid</code> and <code>auth_token</code>  with your unique values.</p>
</section>
<section class="is-hidden">
<div class="docs-note docs-note--error">
<p>Please note: it's okay to hardcode your credentials when getting started, but you should use environment variables to keep them secret before deploying to production. Check out <a href="https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html">how to set environment variables</a> for more information.</p>
</div>
</section>
<section class="is-hidden">
<h4 class="docs-article__section-title" id="replace-the-from_-phone-number"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#replace-the-from_-phone-number">Replace the from_ phone number</a></h4>
<p>Remember that SMS-enabled <a href="https://www.twilio.com/console/phone-numbers/incoming">phone number</a> you bought just a few minutes ago? Go ahead and replace the existing <code>from_</code> number with that one, making sure to use <a href="https://www.twilio.com/docs/glossary/what-e164">E.164</a> formatting:</p>
<p><code>[+][country code][phone number including area code]</code></p>
</section>
<section class="is-hidden">
<h4 class="docs-article__section-title" id="replace-the-to-phone-number"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#replace-the-to-phone-number">Replace the to phone number</a></h4>
<p>Replace the <code>to</code> phone number with your mobile phone number. This can be any phone number that can receive text messages, but it’s a good idea to test with your own phone so you can see the magic happen! As above, you should use E.164 formatting for this value.</p>
</section>
<section class="is-hidden">
<div class="docs-note docs-note--warning">
<p>If you are on a Twilio Trial account, your outgoing SMS messages are limited to phone numbers that you have verified with Twilio. Phone numbers can be verified via your <a href="https://www.twilio.com/console/phone-numbers/verified">Twilio Console's Verified Caller IDs</a>.</p>
<p>When you send an SMS from your free trial phone number, it will always begin with "Sent from a Twilio trial account." We remove this message after you upgrade.</p>
</div>
</section>
<section class="is-hidden">
<p>Save your changes and run this script from your terminal:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">python send_sms.py
</span></pre></div>
<p>That's it! In a few moments, you should receive an SMS from your Twilio number on your phone.</p>
<p>Are your customers in the U.S. or Canada? You can also send them <a href="https://www.twilio.com/docs/glossary/what-is-mms">MMS</a> messages by adding just one line of code. Check out <a href="https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python#send-a-message-containing-media-mms">this guide to sending MMS</a> to see how it's done.</p>
</section>
<section class="is-hidden">
<p>In this code sample, we are making a POST request to the Programmable Messaging API’s Message endpoint in order to create a new outbound message. We are using the <code>twilio-python</code> library’s built-in <code>create</code> method, but you could make this request using the Twilio CLI (that you already installed), <a href="https://curl.haxx.se/">curl</a>, or a request module of your choosing.</p>
<p>Check out the code samples to send an SMS with the Twilio CLI and curl. Don't forget to update the <code>body</code>, <code>to</code>, and <code>from</code> parameters!</p>
</section>
<section class="is-hidden">
<div class="code-sample" data-title="Use the Twilio CLI to send an SMS" id="code-use-the-twilio-cli-to-send-an-sms">
<div class="inline-mode">
<div class="twlo-code code-rail" id="coderail">
<div class="rail-placeholder"></div>
<header class="twlo-code-header rail-title">
<div class="twlo-code-header__title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#linkcode">
<div class="twlo-code-header__title-inner">Use the Twilio CLI to send an SMS</div>
<div class="twlo-code-header__title-loading"></div>
</a>
</div>
<ul class="twlo-code-header__dropdown"></ul>
<div class="twlo-code-header__actions">
<ul class="twlo-code-header__languages"><li class="twlo-code-header__language is-selected" data-sample-language="twilio-cli">twilio-cli</li></ul>
<ul class="twlo-code-header__versions"><li class="twlo-code-header__version is-selected">1.x</li></ul>
</div>
</header>
<div class="twlo-code__sample">
<div class="twlo-code__actions">
<span class="twlo-code__action twlo-code__outdated" style="display: none;">
        You are viewing an outdated version of this SDK.
      </span>
<span class="twlo-code__action clippy">
<svg class="twlo-icon-interface-clipboard" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M16 7v2h-5v2L8 8l3-3v2h5zM8 5H4v1h4V5zm-4 7h5v-1H4v1zm9-1h1v3H2V0h12v5h-1V3H3v10h10v-2zM3 2h10V1H3v1zm1 7v1h3V9H4zm0-1h3V7H4v1z" fill="currentColor"></path></svg>
</span>
<a class="twlo-code__action github hidden" href="https://github.com/" target="_blank">
<svg class="twlo-icon-interface-repo" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M5 3H4V2h1v1zm0 1H4v1h1V4zm0 4H4v1h1V8zm0-2H4v1h1V6zm9-6v14H7v2l-1.5-1L4 16v-2H2V0h12zm-1 11H3v2h1v-1h3v1h6v-2zm0-10H3v9h10V1z" fill="currentColor"></path></svg>
</a>
</div>
<pre class="twlo-code__snippet line-numbers"><code class="codehilite notranslate language-cli"><span class="code-line"><span class="o">#</span> <span class="n">Install</span> <span class="n">the</span> <span class="n">twilio</span><span class="o">-</span><span class="n">cli</span> <span class="k">from</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">twil</span><span class="p">.</span><span class="n">io</span><span class="o">/</span><span class="n">cli</span><br></span><span class="code-line"><br></span><span class="code-line"><span class="n">twilio</span> <span class="n">api</span><span class="p">:</span><span class="n">core</span><span class="p">:</span><span class="n">messages</span><span class="p">:</span><span class="k">create</span> <span class="err">\</span><br></span><span class="code-line">    <span class="c1">--body "Join Earth's mightiest heroes. Like Kevin Bacon." \</span><br></span><span class="code-line">    <span class="c1">--from +15017122661 \</span><br></span><span class="code-line">    <span class="c1">--to +15558675310</span><br></span><span class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<div class="docs-coderail__next" style="display: none;">
<a class="docs-coderail__next-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Next Sample</a>
</div>
<div class="docs-coderail__show_output">
<a class="docs-coderail__show_output-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Show sample response</a>
</div>
</div>
<div class="twlo-code__output" style="display: none;">
<div class="docs-coderail__label">Example JSON API response</div>
<pre class="twlo-code__snippet line-numbers language-json"></pre>
</div>
<div class="twlo-code__info" data-id="code-use-the-twilio-cli-to-send-an-sms"></div>
<script>
//<sl:notranslate>
codeRails = window.twilio.codeRails || {};

codeRails["code-use-the-twilio-cli-to-send-an-sms"] = {
  title: "Use the Twilio CLI to send an SMS",
  sampleType: "server",
  downloadUrl: "",
  githubUrl: "",
  id: "",
  htmlId: "code-use-the-twilio-cli-to-send-an-sms",
  samples: [
    
    {
      "extension": "cli",
      "language": "twilio-cli",
      "version": "1.x",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;o&quot;&gt;#&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;Install&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;the&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;twilio&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;-&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;cli&lt;/span&gt; &lt;span class=&quot;k&quot;&gt;from&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;https&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;//&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;twil&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;io&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;/&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;cli&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;twilio&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;api&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;core&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;messages&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt;&lt;span class=&quot;k&quot;&gt;create&lt;/span&gt; &lt;span class=&quot;err&quot;&gt;\\&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;c1&quot;&gt;--body &amp;quot;Join Earth&amp;#39;s mightiest heroes. Like Kevin Bacon.&amp;quot; \\&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;c1&quot;&gt;--from +15017122661 \\&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;c1&quot;&gt;--to +15558675310&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ],
  outputs: [
    
    {
      "extension": "json",
      "language": "JSON",
      "version": "",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;account_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;api_version&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;2010-04-01&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;body&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Join Earth&amp;#39;s mightiest heroes. Like Kevin Bacon.&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_created&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:31 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_updated&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;direction&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;outbound-api&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_code&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_message&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;from&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+15017122661&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;messaging_service_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;0&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_segments&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;1&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price_unit&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;status&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;subresource_uris&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;nt&quot;&gt;&amp;quot;media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;p&quot;&gt;},&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;to&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+15558675310&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;uri&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;}&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ]
};

window.twilio.codeRails = codeRails;
//</sl:notranslate>
</script>
</div>
<div class="rail-caption">
      This code sample makes a request to the Message resource using the Twilio CLI
    </div>
</div>
<div class="button-mode">
<div class="docs-article__code-cta cursor-hover">
<div class="docs-article__code-cta-cursor-wrap">
<div class="docs-article__code-cta-cursor"></div>
</div>
<div class="docs-article__code-cta-body">
<h4 class="docs-article__code-cta-title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#">Use the Twilio CLI to send an SMS</a>
</h4>
<div class="docs-article__code-cta-path">This code sample makes a request to the Message resource using the Twilio CLI</div>
</div>
<div class="docs-article__code-cta-arrow"></div>
</div>
</div>
</div>
</section>
<section class="is-hidden">
<div class="code-sample" data-title="Use curl to send an SMS" id="code-use-curl-to-send-an-sms">
<div class="inline-mode">
<div class="twlo-code code-rail" id="coderail">
<div class="rail-placeholder"></div>
<header class="twlo-code-header rail-title">
<div class="twlo-code-header__title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#linkcode">
<div class="twlo-code-header__title-inner">Use curl to send an SMS</div>
<div class="twlo-code-header__title-loading"></div>
</a>
</div>
<ul class="twlo-code-header__dropdown"></ul>
<div class="twlo-code-header__actions">
<ul class="twlo-code-header__languages"><li class="twlo-code-header__language is-selected" data-sample-language="curl">curl</li></ul>
<ul class="twlo-code-header__versions"><li class="twlo-code-header__version is-selected">json</li></ul>
</div>
</header>
<div class="twlo-code__sample">
<div class="twlo-code__actions">
<span class="twlo-code__action twlo-code__outdated" style="display: none;">
        You are viewing an outdated version of this SDK.
      </span>
<span class="twlo-code__action clippy">
<svg class="twlo-icon-interface-clipboard" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M16 7v2h-5v2L8 8l3-3v2h5zM8 5H4v1h4V5zm-4 7h5v-1H4v1zm9-1h1v3H2V0h12v5h-1V3H3v10h10v-2zM3 2h10V1H3v1zm1 7v1h3V9H4zm0-1h3V7H4v1z" fill="currentColor"></path></svg>
</span>
<a class="twlo-code__action github hidden" href="https://github.com/" target="_blank">
<svg class="twlo-icon-interface-repo" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M5 3H4V2h1v1zm0 1H4v1h1V4zm0 4H4v1h1V8zm0-2H4v1h1V6zm9-6v14H7v2l-1.5-1L4 16v-2H2V0h12zm-1 11H3v2h1v-1h3v1h6v-2zm0-10H3v9h10V1z" fill="currentColor"></path></svg>
</a>
</div>
<pre class="twlo-code__snippet line-numbers"><code class="codehilite notranslate language-curl"><span class="code-line">curl -X POST https://api.twilio.com/2010-04-01/Accounts/<span class="nv">$TWILIO_ACCOUNT_SID</span>/Messages.json <span class="se">\</span><br></span><span class="code-line">--data-urlencode <span class="s2">"Body=Join Earth's mightiest heroes. Like Kevin Bacon."</span> <span class="se">\</span><br></span><span class="code-line">--data-urlencode <span class="s2">"From=+15017122661"</span> <span class="se">\</span><br></span><span class="code-line">--data-urlencode <span class="s2">"To=+15558675310"</span> <span class="se">\</span><br></span><span class="code-line">-u <span class="nv">$TWILIO_ACCOUNT_SID</span>:<span class="nv">$TWILIO_AUTH_TOKEN</span><br></span><span class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<div class="docs-coderail__next" style="display: none;">
<a class="docs-coderail__next-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Next Sample</a>
</div>
<div class="docs-coderail__show_output">
<a class="docs-coderail__show_output-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Show sample response</a>
</div>
</div>
<div class="twlo-code__output" style="display: none;">
<div class="docs-coderail__label">Example JSON API response</div>
<pre class="twlo-code__snippet line-numbers language-json"></pre>
</div>
<div class="twlo-code__info" data-id="code-use-curl-to-send-an-sms"></div>
<script>
//<sl:notranslate>
codeRails = window.twilio.codeRails || {};

codeRails["code-use-curl-to-send-an-sms"] = {
  title: "Use curl to send an SMS",
  sampleType: "server",
  downloadUrl: "",
  githubUrl: "",
  id: "",
  htmlId: "code-use-curl-to-send-an-sms",
  samples: [
    
    {
      "extension": "curl",
      "language": "curl",
      "version": "json",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;curl -X POST https://api.twilio.com/2010-04-01/Accounts/&lt;span class=&quot;nv&quot;&gt;$TWILIO_ACCOUNT_SID&lt;/span&gt;/Messages.json &lt;span class=&quot;se&quot;&gt;\\&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;--data-urlencode &lt;span class=&quot;s2&quot;&gt;&amp;quot;Body=Join Earth&amp;#39;s mightiest heroes. Like Kevin Bacon.&amp;quot;&lt;/span&gt; &lt;span class=&quot;se&quot;&gt;\\&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;--data-urlencode &lt;span class=&quot;s2&quot;&gt;&amp;quot;From=+15017122661&amp;quot;&lt;/span&gt; &lt;span class=&quot;se&quot;&gt;\\&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;--data-urlencode &lt;span class=&quot;s2&quot;&gt;&amp;quot;To=+15558675310&amp;quot;&lt;/span&gt; &lt;span class=&quot;se&quot;&gt;\\&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;-u &lt;span class=&quot;nv&quot;&gt;$TWILIO_ACCOUNT_SID&lt;/span&gt;:&lt;span class=&quot;nv&quot;&gt;$TWILIO_AUTH_TOKEN&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ],
  outputs: [
    
    {
      "extension": "json",
      "language": "JSON",
      "version": "",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;account_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;api_version&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;2010-04-01&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;body&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Join Earth&amp;#39;s mightiest heroes. Like Kevin Bacon.&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_created&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:31 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_updated&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;direction&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;outbound-api&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_code&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_message&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;from&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+15017122661&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;messaging_service_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;0&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_segments&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;1&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price_unit&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;status&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;subresource_uris&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;nt&quot;&gt;&amp;quot;media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;p&quot;&gt;},&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;to&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+15558675310&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;uri&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;}&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ]
};

window.twilio.codeRails = codeRails;
//</sl:notranslate>
</script>
</div>
<div class="rail-caption">
      This code sample makes a request to the Message resource using curl
    </div>
</div>
<div class="button-mode">
<div class="docs-article__code-cta cursor-hover">
<div class="docs-article__code-cta-cursor-wrap">
<div class="docs-article__code-cta-cursor"></div>
</div>
<div class="docs-article__code-cta-body">
<h4 class="docs-article__code-cta-title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#">Use curl to send an SMS</a>
</h4>
<div class="docs-article__code-cta-path">This code sample makes a request to the Message resource using curl</div>
</div>
<div class="docs-article__code-cta-arrow"></div>
</div>
</div>
</div>
</section>
<section class="docs-article__next_step is-hidden">
<a class="twlo-btn cursor-hover" href="https://www.twilio.com/docs/sms/quickstart/python#">
  I got the message. What's next?
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="set-up-a-twilio-messaging-service"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#set-up-a-twilio-messaging-service">Set up a Twilio Messaging Service</a></h2>
<p>Congratulations, you’ve sent your first SMS with Twilio Programmable Messaging and received it on your personal device.</p>
<p>At this point, we have acquired one Twilio phone number and used it to send one outbound SMS. You can imagine a time in the not-so-distant future where you'll need a more robust, feature-rich way to send messages, such as:</p>
<ul class="docs-article__list">
<li>sending many messages over a short period of time</li>
<li>handling opt-ins and opt-outs</li>
<li>ensuring that your customers always receive a consistent messaging experience with the same phone number.</li>
</ul>
<p>In the next part of the Quickstart, we’ll walk through setting up your first <strong>Messaging Service</strong>. You can think of a Messaging Service as a container to hold all of your available phone numbers (and other senders) and comes with features that you may need along your messaging journey.</p>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="create-a-messaging-service-with-your-phone-number"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#create-a-messaging-service-with-your-phone-number">Create a Messaging Service with your phone number</a></h2>
<p>Run the following Twilio CLI command to create a Messaging Service that we will use to send our first programmable SMS.</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">twilio api:messaging:v1:services:create --friendly-name "My first Messaging Service"
</span></pre></div>
<p>Take note of the Messaging Service SID (It starts with “MGXXX...”). We'll need it to send our next message.</p>
<p>Next, add the phone number you just purchased. Forgot the number already? No worries, you can list it with the Twilio CLI:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">twilio phone-numbers:list
</span><span class="code-line"># Grab the SID ("PNXXXX...") of your number
</span></pre></div>
<p>Add your phone number to your newly created Messaging Service with the following command:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">twilio api:messaging:v1:services:phone-numbers:create --service-sid MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX --phone-number-sid PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
</span></pre></div>
</section>
<section class="docs-article__next_step is-hidden">
<a class="twlo-btn cursor-hover" href="https://www.twilio.com/docs/sms/quickstart/python#">
  Okay, I'm ready to send from my service.
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="send-an-sms-from-your-messaging-service"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#send-an-sms-from-your-messaging-service">Send an SMS from your Messaging Service</a></h2>
<p>Sending an outbound SMS from a Messaging Service is similar to sending from an individual Twilio phone number. The primary difference is replacing the <code>from_</code> parameter with the <code>messaging_service_sid</code> to indicate that you are sending from a phone number within your Messaging Service’s sender pool. (Currently, there is only one phone number in your sender pool, so we'll be sending from that one.)</p>
</section>
<section class="is-hidden">
<div class="code-sample" data-title="Send an SMS using a Messaging Service" id="code-send-an-sms-using-a-messaging-service">
<div class="inline-mode">
<div class="twlo-code code-rail" id="coderail">
<div class="rail-placeholder"></div>
<header class="twlo-code-header rail-title">
<div class="twlo-code-header__title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#linkcode">
<div class="twlo-code-header__title-inner">Send an SMS using a Messaging Service</div>
<div class="twlo-code-header__title-loading"></div>
</a>
</div>
<ul class="twlo-code-header__dropdown"></ul>
<div class="twlo-code-header__actions">
<ul class="twlo-code-header__languages"><li class="twlo-code-header__language is-selected" data-sample-language="Python">Python</li></ul>
<ul class="twlo-code-header__versions"><li class="twlo-code-header__version is-selected">6.x</li></ul>
</div>
</header>
<div class="twlo-code__sample">
<div class="twlo-code__actions">
<span class="twlo-code__action twlo-code__outdated" style="display: none;">
        You are viewing an outdated version of this SDK.
      </span>
<span class="twlo-code__action clippy">
<svg class="twlo-icon-interface-clipboard" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M16 7v2h-5v2L8 8l3-3v2h5zM8 5H4v1h4V5zm-4 7h5v-1H4v1zm9-1h1v3H2V0h12v5h-1V3H3v10h10v-2zM3 2h10V1H3v1zm1 7v1h3V9H4zm0-1h3V7H4v1z" fill="currentColor"></path></svg>
</span>
<a class="twlo-code__action github hidden" href="https://github.com/" target="_blank">
<svg class="twlo-icon-interface-repo" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M5 3H4V2h1v1zm0 1H4v1h1V4zm0 4H4v1h1V8zm0-2H4v1h1V6zm9-6v14H7v2l-1.5-1L4 16v-2H2V0h12zm-1 11H3v2h1v-1h3v1h6v-2zm0-10H3v9h10V1z" fill="currentColor"></path></svg>
</a>
</div>
<pre class="twlo-code__snippet line-numbers"><code class="codehilite notranslate language-py"><span class="code-line"><span class="c1"># Download the helper library from https://www.twilio.com/docs/python/install</span><br></span><span class="code-line"><span class="kn">import</span> <span class="nn">os</span><br></span><span class="code-line"><span class="kn">from</span> <span class="nn">twilio.rest</span> <span class="kn">import</span> <span class="n">Client</span><br></span><span class="code-line"><br></span><span class="code-line"><br></span><span class="code-line"><span class="c1"># Your Account Sid and Auth Token from twilio.com/console</span><br></span><span class="code-line"><span class="c1"># and set the environment variables. See http://twil.io/secure</span><br></span><span class="code-line"><span class="n">account_sid</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s1">'TWILIO_ACCOUNT_SID'</span><span class="p">]</span><br></span><span class="code-line"><span class="n">auth_token</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s1">'TWILIO_AUTH_TOKEN'</span><span class="p">]</span><br></span><span class="code-line"><span class="n">client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="n">account_sid</span><span class="p">,</span> <span class="n">auth_token</span><span class="p">)</span><br></span><span class="code-line"><br></span><span class="code-line"><span class="n">message</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">messages</span> \<br></span><span class="code-line">    <span class="o">.</span><span class="n">create</span><span class="p">(</span><br></span><span class="code-line">         <span class="n">messaging_service_sid</span><span class="o">=</span><span class="s1">'MG9752274e9e519418a7406176694466fa'</span><span class="p">,</span><br></span><span class="code-line">         <span class="n">body</span><span class="o">=</span><span class="s1">'body'</span><span class="p">,</span><br></span><span class="code-line">         <span class="n">to</span><span class="o">=</span><span class="s1">'+15558675310'</span><br></span><span class="code-line">     <span class="p">)</span><br></span><span class="code-line"><br></span><span class="code-line"><span class="nb">print</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">sid</span><span class="p">)</span><br></span><span class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<div class="docs-coderail__next" style="display: none;">
<a class="docs-coderail__next-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Next Sample</a>
</div>
<div class="docs-coderail__show_output">
<a class="docs-coderail__show_output-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Show sample response</a>
</div>
</div>
<div class="twlo-code__output" style="display: none;">
<div class="docs-coderail__label">Example JSON API response</div>
<pre class="twlo-code__snippet line-numbers language-json"></pre>
</div>
<div class="twlo-code__info" data-id="code-send-an-sms-using-a-messaging-service"></div>
<script>
//<sl:notranslate>
codeRails = window.twilio.codeRails || {};

codeRails["code-send-an-sms-using-a-messaging-service"] = {
  title: "Send an SMS using a Messaging Service",
  sampleType: "server",
  downloadUrl: "",
  githubUrl: "",
  id: "",
  htmlId: "code-send-an-sms-using-a-messaging-service",
  samples: [
    
    {
      "extension": "py",
      "language": "Python",
      "version": "6.x",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;c1&quot;&gt;# Download the helper library from https://www.twilio.com/docs/python/install&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;kn&quot;&gt;import&lt;/span&gt; &lt;span class=&quot;nn&quot;&gt;os&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;kn&quot;&gt;from&lt;/span&gt; &lt;span class=&quot;nn&quot;&gt;twilio.rest&lt;/span&gt; &lt;span class=&quot;kn&quot;&gt;import&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;Client&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;c1&quot;&gt;# Your Account Sid and Auth Token from twilio.com/console&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;c1&quot;&gt;# and set the environment variables. See http://twil.io/secure&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;account_sid&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;os&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;environ&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;[&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;TWILIO_ACCOUNT_SID&amp;#39;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;]&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;auth_token&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;os&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;environ&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;[&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;TWILIO_AUTH_TOKEN&amp;#39;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;]&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;client&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;Client&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;(&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;account_sid&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;auth_token&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;)&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;n&quot;&gt;message&lt;/span&gt; &lt;span class=&quot;o&quot;&gt;=&lt;/span&gt; &lt;span class=&quot;n&quot;&gt;client&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;messages&lt;/span&gt; \\&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;create&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;(&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;         &lt;span class=&quot;n&quot;&gt;messaging_service_sid&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;=&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;MG9752274e9e519418a7406176694466fa&amp;#39;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;         &lt;span class=&quot;n&quot;&gt;body&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;=&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;body&amp;#39;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;         &lt;span class=&quot;n&quot;&gt;to&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;=&lt;/span&gt;&lt;span class=&quot;s1&quot;&gt;&amp;#39;+15558675310&amp;#39;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;     &lt;span class=&quot;p&quot;&gt;)&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;nb&quot;&gt;print&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;(&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;message&lt;/span&gt;&lt;span class=&quot;o&quot;&gt;.&lt;/span&gt;&lt;span class=&quot;n&quot;&gt;sid&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;)&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ],
  outputs: [
    
    {
      "extension": "json",
      "language": "JSON",
      "version": "",
      "filename": "",
      "codeId": "&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;account_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;api_version&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;2010-04-01&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;body&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Hello! 👍&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_created&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:31 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;date_updated&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;Thu, 30 Jul 2015 20:12:33 +0000&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;direction&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;outbound-api&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_code&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;error_message&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;from&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+14155552345&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;messaging_service_sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;MG9752274e9e519418a7406176694466fa&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;0&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;num_segments&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;1&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;price_unit&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;kc&quot;&gt;null&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;sid&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;status&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;sent&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;subresource_uris&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;p&quot;&gt;{&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;    &lt;span class=&quot;nt&quot;&gt;&amp;quot;media&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;p&quot;&gt;},&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;to&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;+15558675310&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;,&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;  &lt;span class=&quot;nt&quot;&gt;&amp;quot;uri&amp;quot;&lt;/span&gt;&lt;span class=&quot;p&quot;&gt;:&lt;/span&gt; &lt;span class=&quot;s2&quot;&gt;&amp;quot;/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json&amp;quot;&lt;/span&gt;&lt;br&gt;&lt;/span&gt;&lt;span class=&quot;code-line&quot;&gt;&lt;span class=&quot;p&quot;&gt;}&lt;/span&gt;&lt;br&gt;&lt;/span&gt;"
    },
    
  ]
};

window.twilio.codeRails = codeRails;
//</sl:notranslate>
</script>
</div>
<div class="rail-caption">
      This code creates a new instance of the Message resource, this time with a messaging_service_sid parameter
    </div>
</div>
<div class="button-mode">
<div class="docs-article__code-cta cursor-hover">
<div class="docs-article__code-cta-cursor-wrap">
<div class="docs-article__code-cta-cursor"></div>
</div>
<div class="docs-article__code-cta-body">
<h4 class="docs-article__code-cta-title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#">Send an SMS using a Messaging Service</a>
</h4>
<div class="docs-article__code-cta-path">This code creates a new instance of the Message resource, this time with a messaging_service_sid parameter</div>
</div>
<div class="docs-article__code-cta-arrow"></div>
</div>
</div>
</div>
</section>
<section class="is-hidden">
<h4 class="docs-article__section-title" id="replace-the-messaging_service_sid-parameter"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#replace-the-messaging_service_sid-parameter">Replace the messaging_service_sid parameter</a></h4>
<p>Remember that Messaging Service you just created? Instead of the <code>from_</code> parameter and your phone number, use the  <code>messaging_service_sid</code> parameter with the "MGXXXX..." of your Messaging Service SID. Save your changes and run this script from your terminal:</p>
<div class="codehilite language-text"><pre class="twlo-code language-text" data-line=""><span class="code-line">python send_sms.py
</span></pre></div>
<p>And that’s in to send an SMS using a Twilio Messaging Service! In a few seconds, you should receive a second SMS on your phone from your Twilio phone number. The Messaging Service seamlessly selected your number from its Sender Pool to send that second outbound message.</p>
</section>
<section class="docs-article__next_step is-hidden">
<a class="twlo-btn cursor-hover" href="https://www.twilio.com/docs/sms/quickstart/python#">
  It worked! All done - what's next?
  <span class="twlo-btn__cursor-arrow"></span>
</a>
</section>
<section class="is-hidden">
<h2 class="docs-article__section-title" id="where-to-next"><a class="toclink" href="https://www.twilio.com/docs/sms/quickstart/python#where-to-next">Where to next?</a></h2>
<p>Now that you've send your first SMS messages, check out the following resources to continue your messaging journey with Twilio:</p>
<ul class="docs-article__list">
<li>Learn about inbound messages with <a href="https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply">Receive and Reply to SMS and MMS messages</a></li>
<li>Want to send with WhatsApp? Check out our <a href="https://www.twilio.com/docs/whatsapp/quickstart/python">WhatsApp Quickstart for Python</a> and our guide to <a href="https://www.twilio.com/docs/whatsapp/tutorial/send-whatsapp-notification-messages-templates">Sending WhatsApp Notifications with Templates</a></li>
<li>Build <a href="https://www.twilio.com/docs/sms/tutorials/server-notifications">Server Notifications with Twilio Programmable Messaging</a></li>
<li>Dive into the <a href="https://www.twilio.com/docs/sms/api">API Reference documentation for Twilio SMS</a></li>
<li><a href="https://www.twilio.com/docs/sms/tutorials/how-to-confirm-delivery-python">Track the delivery status of your messages</a> with Python</li>
</ul>
<p>We can't wait to see what you build!</p>
</section>
<div class="rating-wrapper is-hidden">
<div class="rating-stars" data-rating="0">
<span class="rating-label">Rate this page:</span>
<ol><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li><li class="rating-star"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path class="star-path" d="M8 0l2 6h6l-5 4 2 6-5-4-5 4 2-6-5-4h6l2-6z"></path>
            </svg></li></ol></div>
</div>
<section class="is-hidden">
<div class="docs-help">
<h4 class="docs-help__title">Need some help?</h4>
<p class="docs-help__body">
      We all do sometimes; code is hard. Get help now from our
      <a href="https://support.twilio.com/hc/en-us">support team</a>, or lean on
      the wisdom of the crowd browsing the
      <a href="http://stackoverflow.com/questions/tagged/twilio">Twilio tag</a>
      on Stack Overflow.</p>
</div>
</section>
<footer class="docs-article-footer is-hidden">
<ul class="docs-article-footer__list">
<li class="docs-article-footer__list-item">
<a class="docs-article-footer__link" href="https://www.twilio.com/legal/tos">Terms of Service</a>
</li>
<li class="docs-article-footer__list-item">
<a class="docs-article-footer__link" href="https://www.twilio.com/legal/privacy">Privacy Policy</a>
</li>
<li class="docs-article-footer__list-item">Copyright © 2021 Twilio Inc.</li>
</ul>
</footer>
</article>
</div>
<div class="twlo-code code-rail docs-coderail docs-layout-column" data-column-mode="true" id="coderail" style="height: 559px;">
<div class="rail-placeholder"></div>
<header class="twlo-code-header rail-title">
<div class="twlo-code-header__title">
<a href="https://www.twilio.com/docs/sms/quickstart/python#linkcode">
<div class="twlo-code-header__title-inner">Send an SMS Using Twilio</div>
<div class="twlo-code-header__title-loading"></div>
</a>
<svg class="twlo-icon-interface-dropdown" height="18" viewBox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><path d="M15 7l-6 6-6-6V6h1l5 5 5-5h1v1z" fill="currentColor"></path></svg>
</div>
<ul class="twlo-code-header__dropdown"></ul>
<div class="twlo-code-header__actions">
<ul class="twlo-code-header__languages"><li class="twlo-code-header__language is-selected" data-sample-language="Python">Python</li></ul>
<ul class="twlo-code-header__versions"><li class="twlo-code-header__version is-selected">6.x</li></ul>
</div>
</header>
<div class="twlo-code__sample">
<div class="twlo-code__actions">
<span class="twlo-code__action twlo-code__outdated" style="display: none;">
        You are viewing an outdated version of this SDK.
      </span>
<span class="twlo-code__action clippy">
<svg class="twlo-icon-interface-clipboard" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M16 7v2h-5v2L8 8l3-3v2h5zM8 5H4v1h4V5zm-4 7h5v-1H4v1zm9-1h1v3H2V0h12v5h-1V3H3v10h10v-2zM3 2h10V1H3v1zm1 7v1h3V9H4zm0-1h3V7H4v1z" fill="currentColor"></path></svg>
</span>
<a class="twlo-code__action github hidden" href="https://github.com/" target="_blank">
<svg class="twlo-icon-interface-repo" height="16" viewBox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg"><path d="M5 3H4V2h1v1zm0 1H4v1h1V4zm0 4H4v1h1V8zm0-2H4v1h1V6zm9-6v14H7v2l-1.5-1L4 16v-2H2V0h12zm-1 11H3v2h1v-1h3v1h6v-2zm0-10H3v9h10V1z" fill="currentColor"></path></svg>
</a>
</div>
<pre class="twlo-code__snippet line-numbers"><code class="codehilite notranslate language-py"><span class="code-line"><span class="c1"># Download the helper library from https://www.twilio.com/docs/python/install</span><br></span><span class="code-line"><span class="kn">import</span> <span class="nn">os</span><br></span><span class="code-line"><span class="kn">from</span> <span class="nn">twilio.rest</span> <span class="kn">import</span> <span class="n">Client</span><br></span><span class="code-line"><br></span><span class="code-line"><br></span><span class="code-line"><span class="c1"># Your Account Sid and Auth Token from twilio.com/console</span><br></span><span class="code-line"><span class="c1"># and set the environment variables. See http://twil.io/secure</span><br></span><span class="code-line"><span class="n">account_sid</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s1">'TWILIO_ACCOUNT_SID'</span><span class="p">]</span><br></span><span class="code-line"><span class="n">auth_token</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">[</span><span class="s1">'TWILIO_AUTH_TOKEN'</span><span class="p">]</span><br></span><span class="code-line"><span class="n">client</span> <span class="o">=</span> <span class="n">Client</span><span class="p">(</span><span class="n">account_sid</span><span class="p">,</span> <span class="n">auth_token</span><span class="p">)</span><br></span><span class="code-line"><br></span><span class="code-line"><span class="n">message</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">messages</span> \<br></span><span class="code-line">                <span class="o">.</span><span class="n">create</span><span class="p">(</span><br></span><span class="code-line">                     <span class="n">body</span><span class="o">=</span><span class="s2">"Join Earth's mightiest heroes. Like Kevin Bacon."</span><span class="p">,</span><br></span><span class="code-line">                     <span class="n">from_</span><span class="o">=</span><span class="s1">'+15017122661'</span><span class="p">,</span><br></span><span class="code-line">                     <span class="n">to</span><span class="o">=</span><span class="s1">'+15558675310'</span><br></span><span class="code-line">                 <span class="p">)</span><br></span><span class="code-line"><br></span><span class="code-line"><span class="nb">print</span><span class="p">(</span><span class="n">message</span><span class="o">.</span><span class="n">sid</span><span class="p">)</span><br></span><span class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
<div class="docs-coderail__next">
<a class="docs-coderail__next-link" href="https://www.twilio.com/docs/sms/quickstart/python#">Next Sample</a>
</div>
</div>
<div class="twlo-code__output" style="">
<div class="docs-coderail__label">Example JSON API response</div>
<pre class="twlo-code__snippet line-numbers language-json"><code class="codehilite notranslate"><span class="code-line"><span class="p">{</span><br></span><span class="code-line">  <span class="nt">"account_sid"</span><span class="p">:</span> <span class="s2">"ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"api_version"</span><span class="p">:</span> <span class="s2">"2010-04-01"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"body"</span><span class="p">:</span> <span class="s2">"Join Earth's mightiest heroes. Like Kevin Bacon."</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"date_created"</span><span class="p">:</span> <span class="s2">"Thu, 30 Jul 2015 20:12:31 +0000"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"date_sent"</span><span class="p">:</span> <span class="s2">"Thu, 30 Jul 2015 20:12:33 +0000"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"date_updated"</span><span class="p">:</span> <span class="s2">"Thu, 30 Jul 2015 20:12:33 +0000"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"direction"</span><span class="p">:</span> <span class="s2">"outbound-api"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"error_code"</span><span class="p">:</span> <span class="kc">null</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"error_message"</span><span class="p">:</span> <span class="kc">null</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"from"</span><span class="p">:</span> <span class="s2">"+15017122661"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"messaging_service_sid"</span><span class="p">:</span> <span class="s2">"MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"num_media"</span><span class="p">:</span> <span class="s2">"0"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"num_segments"</span><span class="p">:</span> <span class="s2">"1"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"price"</span><span class="p">:</span> <span class="kc">null</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"price_unit"</span><span class="p">:</span> <span class="kc">null</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"sid"</span><span class="p">:</span> <span class="s2">"SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"status"</span><span class="p">:</span> <span class="s2">"sent"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"subresource_uris"</span><span class="p">:</span> <span class="p">{</span><br></span><span class="code-line">    <span class="nt">"media"</span><span class="p">:</span> <span class="s2">"/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"</span><br></span><span class="code-line">  <span class="p">},</span><br></span><span class="code-line">  <span class="nt">"to"</span><span class="p">:</span> <span class="s2">"+15558675310"</span><span class="p">,</span><br></span><span class="code-line">  <span class="nt">"uri"</span><span class="p">:</span> <span class="s2">"/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"</span><br></span><span class="code-line"><span class="p">}</span><br></span><span class="line-numbers-rows"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></span></code></pre>
</div>
</div>
</main>
</div><script type="text/javascript" id="">var _C={REDACTION_COPY:{EMAIL:"EMAIL_REDACTED"}};function extractParams(){for(var b=[],a,c=/([^&=]+)=?([^&]*)/g,d=window.location.search.substring(1);a=c.exec(d);)b.push([a[1],a[2]]);return b}var urlParams=extractParams(),emailRegex=/(([^<>()\[\]\\.,;:\s@"%]+(\.[^<>()\[\]\\.,;:\s@"%]+)*)|(".+"))(@|%40)((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/g;
urlParams=urlParams.map(function(b){return b.map(function(a){_redactedValue=decodeURIComponent(a).replace(emailRegex,_C.REDACTION_COPY.EMAIL);return _redactedValue===_C.REDACTION_COPY.EMAIL?_redactedValue:a})});
function rewriteURL(b){if(0===b.length)return window.location.protocol+"//"+window.location.host+window.location.pathname+window.location.hash;for(var a="?",c=0;c<b.length;c++)0<c&&(a=a.concat("\x26")),a=a.concat(b[c][0]+"\x3d"+b[c][1]);return window.location.protocol+"//"+window.location.host+window.location.pathname+a+window.location.hash}var newURL=rewriteURL(urlParams);newURL!==window.location.href&&window.history.replaceState({},document.title,newURL);
var newTitle=document.title.replace(emailRegex,_C.REDACTION_COPY.EMAIL);newTitle!==document.title&&(document.title=newTitle);dataLayer.push({event:"piiRedacted"});</script><script type="text/javascript" id="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/notice"></script>

<script type="text/javascript" id="">self._truste_eumap&&dataLayer.push({cm_ctx:"eu",event:"consentManagerLoaded"});dataLayer.push({event:"trustarcLoaded"});var __dispatched__={},__i__=self.postMessage&&setInterval(function(){if(self.PrivacyManagerAPI&&__i__){var b={PrivacyManagerAPI:{action:"getConsentDecision",timestamp:(new Date).getTime(),self:self.location.host}};self.top.postMessage(JSON.stringify(b),"*");__i__=clearInterval(__i__)}},50);
self.addEventListener("message",function(b,a){try{if(b.data&&(a=JSON.parse(b.data))&&(a=a.PrivacyManagerAPI)&&a.capabilities&&"getConsentDecision"==a.action){var d=self.PrivacyManagerAPI.callApi("getGDPRConsentDecision",self.location.host).consentDecision;d&&d.forEach(function(c){__dispatched__[c]||(self.dataLayer&&self.dataLayer.push({event:"GDPR Pref Allows "+c}),__dispatched__[c]=1)})}}catch(c){}});</script><script type="text/javascript" id="">var _kiq=_kiq||[];(function(){setTimeout(function(){var a=document,b=a.getElementsByTagName("script")[0];a=a.createElement("script");a.type="text/javascript";a.async=!0;a.src="//s3.amazonaws.com/ki.js/60855/dM4.js";b.parentNode.insertBefore(a,b)},1)})();"twilio"in window&&twilio.account&&twilio.account.sid&&_kiq.push(["identify",twilio.account.sid]);</script>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("dataProcessingOptions",[]);fbq("init","1040773425961662");fbq("track","PageView");</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=1040773425961662&amp;ev=PageView&amp;noscript=1"></noscript>


<script type="text/javascript" id="">!function(b,c,d,a){b.twq||(a=b.twq=function(){a.exe?a.exe.apply(a,arguments):a.queue.push(arguments)},a.version="1",a.queue=[],t=c.createElement(d),t.async=!0,t.src="//static.ads-twitter.com/uwt.js",s=c.getElementsByTagName(d)[0],s.parentNode.insertBefore(t,s))}(window,document,"script");twq("init","nv97q");twq("track","PageView");</script>
<script type="text/javascript" id="">var getCookie;
if("twilio"in window&&(!twilio.user||"full"===twilio.user.access)){getCookie=function(a){var b="; "+document.cookie;a=b.split("; "+a+"\x3d");if(2==a.length)return a.pop().split(";").shift()};var _session_id=getCookie("tw-session-id");_session_id||(document.cookie="tw-session-id\x3d"+Date.now()+Math.random()+";path\x3d/;domain\x3d.twilio.com",_session_id=getCookie("tw-session-id"));var sid="AC53eb918d457ac68fb17d2273966afa35",_sift=window._sift=window._sift||[];_sift.push(["_setAccount","316b238f93"]);_sift.push(["_setUserId",
sid]);_sift.push(["_setSessionId",_session_id]);_sift.push(["_trackPageview"]);(function(){function a(){var b=document.createElement("script");b.type="text/javascript";b.async=!0;b.src=("https:"===document.location.protocol?"https://":"http://")+"cdn.siftscience.com/s.js";var c=document.getElementsByTagName("script")[0];c.parentNode.insertBefore(b,c)}window.attachEvent?window.attachEvent("onload",a):window.addEventListener("load",a,!1)})()};</script><script type="text/javascript" id="">window.heap=window.heap||[];
heap.load=function(b,a){window.heap.appid=b;window.heap.config=a=a||{};var c=a.forceSSL||"https:"===document.location.protocol;a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src=(c?"https:":"http:")+"//cdn.heapanalytics.com/js/heap-"+b+".js";b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b);b=function(d){return function(){heap.push([d].concat(Array.prototype.slice.call(arguments,0)))}};a="addEventProperties addUserProperties clearEventProperties identify removeEventProperty setEventProperties track unsetEventProperty resetIdentity".split(" ");for(c=
0;c<a.length;c++)heap[a[c]]=b(a[c])};heap.load(google_tag_manager["GTM-MWRD6S"].macro(4),{disableTextCapture:!0});google_tag_manager["GTM-MWRD6S"].macro(5)?heap.identify(google_tag_manager["GTM-MWRD6S"].macro(6),"User ID"):heap.identify(google_tag_manager["GTM-MWRD6S"].macro(7),"Visitor Id");</script>
<script type="text/javascript" id="">var _qevents=_qevents||[];(function(){var a=document.createElement("script");a.src=("https:"==document.location.protocol?"https://secure":"http://edge")+".quantserve.com/quant.js";a.async=!0;a.type="text/javascript";var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b)})();_qevents.push({qacct:"p-efmoRQHrDUXig"});</script>
<noscript>
 <img src="//pixel.quantserve.com/pixel/p-efmoRQHrDUXig.gif?labels=_fp.event.Default" style="display: none;" border="0" height="1" width="1" alt="Quantcast">
</noscript>


<script type="text/javascript" id="">var bfId="bxIiMMuhVmgMMH42",bfSession=.041666666666666664;(function(){var a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src=("https:"===document.location.protocol?"https://":"http://")+"munchkin.brightfunnel.com/js/build/bf-munchkin.min.js";var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b)})();</script>
<script type="text/javascript" id="">var playerLinks=document.querySelectorAll(".watch-video");if(0<playerLinks.length){var tag=document.createElement("script");tag.src="https://www.youtube.com/iframe_api";var firstScriptTag=document.getElementsByTagName("script")[0];firstScriptTag.parentNode.insertBefore(tag,firstScriptTag)}
for(var players=document.querySelectorAll(".video__canvas"),i=0;i<players.length;i++){var playerEl=players[i].getElementsByTagName("video"),playerObj;playerEl&&(player=videojs(playerEl[0].getAttribute("id")))&&(player.on("play",function(){0==Math.floor(player.currentTime())&&dataLayer.push({event:"gtmEvent",eventCategory:"video",eventAction:"video start",eventLabel:player.mediainfo.name})}),player.on("pause",function(){Math.floor(player.currentTime())==Math.floor(player.duration())&&dataLayer.push({event:"gtmEvent",
eventCategory:"video",eventAction:"video complete",eventLabel:player.mediainfo.name})}))}playerLinks=document.querySelectorAll(".video-content__play-link");
if(0<playerLinks.length)for(tag=document.createElement("script"),tag.src="https://player.vimeo.com/api/player.js",firstScriptTag=document.getElementsByTagName("script")[0],firstScriptTag.parentNode.insertBefore(tag,firstScriptTag),i=0;i<playerLinks.length;i++){var el=playerLinks[i];el.addEventListener("click",function(b){setTimeout(function(){var d=document.querySelectorAll(".mfp-iframe");d[0].setAttribute("id","vimeoPlayer");var a=new Vimeo.Player("vimeoPlayer");a.on("play",function(){a.started||
(a.started=!0,a.getVideoTitle().then(function(c){dataLayer.push({event:"gtmEvent",eventCategory:"video",eventAction:"video start",eventLabel:c})})["catch"](function(c){}))});a.on("ended",function(){a.getVideoTitle().then(function(c){dataLayer.push({event:"gtmEvent",eventCategory:"video",eventAction:"video complete",eventLabel:c})})["catch"](function(c){})})},500)})}var vids=document.querySelectorAll(".video-wrapper");
if(0<vids.length)for(i=0;i<vids.length;i++)if(players=vids[i].getElementsByTagName("video"),0<players.length)for(var j=0;j<players.length;j++){var p=players[j];p.addEventListener("play",function(b){0==Math.floor(b.target.currentTime)&&dataLayer.push({event:"gtmEvent",eventCategory:"video",eventAction:"video start",eventLabel:b.target.currentSrc})});p.addEventListener("ended",function(b){dataLayer.push({event:"gtmEvent",eventCategory:"video",eventAction:"video complete",eventLabel:b.target.currentSrc})})};</script><script type="text/javascript" id="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/pa-5cc1d870e98940001600009c.js.download"></script><script type="text/javascript" id="">(function(){function b(){!1===c&&(c=!0,Munchkin.init("294-TKB-300",{asyncOnly:!0}))}var c=!1,a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="//munchkin.marketo.net/munchkin.js";a.onreadystatechange=function(){"complete"!=this.readyState&&"loaded"!=this.readyState||b()};a.onload=b;document.getElementsByTagName("head")[0].appendChild(a)})();</script><script type="text/javascript" id="">!function(b){var a=b.clearbit=b.clearbit||[];if(!a.initialize)if(a.invoked)b.console&&console.error&&console.error("Clearbit snippet included twice.");else{a.invoked=!0;a.methods="trackSubmit trackClick trackLink trackForm pageview identify reset group track ready alias page once off on".split(" ");a.factory=function(c){return function(){var d=Array.prototype.slice.call(arguments);d.unshift(c);a.push(d);return a}};for(b=0;b<a.methods.length;b++){var e=a.methods[b];a[e]=a.factory(e)}a.load=function(c){var d=
document.createElement("script");d.async=!0;d.src=("https:"===document.location.protocol?"https://":"http://")+"x.clearbitjs.com/v1/"+c+"/clearbit.min.js";c=document.getElementsByTagName("script")[0];c.parentNode.insertBefore(d,c)};a.SNIPPET_VERSION="3.1.0";a.load("pk_0805aa32b9848e8e93733f7054c45487");a.page()}}(window);</script><script type="text/javascript" id="">function pushToDataLayer(a){a={reveal:a};dataLayer.push(a);dataLayer.push({event:"Clearbit Loaded"});return!0};</script>
<script type="text/javascript" id="" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/reveal"></script><script type="text/javascript" id="">window._6si=window._6si||[];window._6si.push(["enableEventTracking",!0]);window._6si.push(["setToken","cd4ba9100b4470e1dde33ce034e651c7"]);window._6si.push(["setEndpoint","b.6sc.co"]);(function(){var a=document.createElement("script");a.type="text/javascript";a.async=!0;a.src="//j.6sc.co/6si.min.js";var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b)})();</script>


<div class="twlo-modal-overlay" id="feedback-form-modal">
<form action="https://www.twilio.com/docs/submit-feedback" id="feedback" method="POST">
<div class="twlo-modal">
<span class="twlo-modal__close close">
<svg class="icon-close" fill="#233659" height="18" viewBox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg">
<path d="M15 4l-5 5 5 5v1h-1l-5-5-5 5H3v-1l5-5-5-5V3h1l5 5 5-5h1v1z"></path>
</svg>
</span>
<h2 class="twlo-modal__title">Thank you for your feedback!</h2>
<p class="twlo-modal__body">
We are always striving to improve our documentation quality, and your feedback is valuable to us. How could this documentation serve you better?
</p>
<input name="star_rating" type="hidden" value="">
<input name="page" type="hidden" value="1161">
<input name="page_live_revision" type="hidden" value="386903">
<input name="requested_path" type="hidden" value="/docs/sms/quickstart/python">
<input name="csrfmiddlewaretoken" type="hidden" value="jQ2rftq127IaPDGf3xN44DWoXbjLoUwHc80y4UQfSMTYxNzIwMzcxMy42NTUyMTI">
<input name="recaptcha" type="hidden" value="">
<div class="feedback-countries hidden">
<label for="countries">If applicable fill in the countries where you are using Twilio</label><br>
<input id="countries" name="countries" value=""><br>
</div>
<textarea class="twlo-modal__textarea" name="comment" placeholder="Suggestions..."></textarea>
<button class="twlo-btn" id="feedback-submit-btn" type="button">Send your suggestions</button>
<div class="twlo-modal__footer">
<div class="talk-to-support">
<a href="https://www.twilio.com/console/support/tickets/create" target="_blank">Talk to Support</a>
</div>
<div class="rc-anchor-pt">
          Protected by reCAPTCHA – <a href="https://www.google.com/intl/en/policies/privacy/" target="_blank">Privacy</a><span aria-hidden="true" role="presentation"> - </span><a href="https://www.google.com/intl/en/policies/terms/" target="_blank">Terms</a>
</div>
</div>
</div>
</form>
</div>
<div class="twlo-modal-overlay" id="sending-feedback-modal">
<div class="twlo-loading loading-no-bg">
<div class="twlo-loading__inner">
<div class="twlo-loading__spinner">
<svg><circle cx="25" cy="25" fill="none" r="20" stroke-miterlimit="10" stroke-width="2"></circle></svg>
</div>
<div class="twlo-loading__message">
        Sending your feedback...
      </div>
</div>
</div>
</div>
<div class="twlo-modal-overlay" id="feedback-sent-modal">
<div class="twlo-modal__submit-message">
  🎉 Thank you for your feedback!
  </div>
</div>
<div class="twlo-modal-overlay" id="feedback-error-modal">
<div class="twlo-modal__submit-message">
  Something went wrong. Please try again.
  </div>
</div>
<div class="twlo-modal-overlay" id="feedback-referral-modal">
<div class="twlo-modal referral">
<span class="twlo-modal__close close">
<svg class="icon-close" fill="#233659" height="18" viewBox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg">
<path d="M15 4l-5 5 5 5v1h-1l-5-5-5 5H3v-1l5-5-5-5V3h1l5 5 5-5h1v1z"></path>
</svg>
</span>
<h2 class="twlo-modal__title">Thanks for your feedback!</h2>
<p class="twlo-modal__body">Refer us and get $10 in 3 simple steps!</p>
<div class="steps-container">
<div class="step">
<h4>Step 1</h4>
<div class="card">Get link</div>
<p>Get a free personal referral link <a href="https://www.twilio.com/console?modal=referral" target="_blank">here</a></p>
</div>
<div class="step">
<h4>Step 2</h4>
<div class="card">Give $10</div>
<p>Your user signs up and upgrade using link</p>
</div>
<div class="step">
<h4>Step 3</h4>
<div class="card">Get $10</div>
<p>1,250 free SMSes <br>OR 1,000 free voice mins <br>OR 12,000 chats <br>OR more</p>
</div>
</div>
<div class="twlo-modal__footer">
<a href="https://www.twilio.com/blog/announcing-twilio-referral-program" target="_blank">Learn more about the referral program</a>
</div>
</div>
</div>

<script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/vendor.min.722f741d2.js.download"></script>
<!-- Mixpanel -->
<script type="text/javascript">(function(e,b){if(!b.__SV){var a,f,i,g;window.mixpanel=b;a=e.createElement("script");a.type="text/javascript";a.async=!0;a.src=("https:"===e.location.protocol?"https:":"http:")+'//cdn.mxpnl.com/libs/mixpanel-2.2.min.js';f=e.getElementsByTagName("script")[0];f.parentNode.insertBefore(a,f);b._i=[];b.init=function(a,e,d){function f(b,h){var a=h.split(".");2==a.length&&(b=b[a[0]],h=a[1]);b[h]=function(){b.push([h].concat(Array.prototype.slice.call(arguments,0)))}}var c=b;"undefined"!==
  typeof d?c=b[d]=[]:d="mixpanel";c.people=c.people||[];c.toString=function(b){var a="mixpanel";"mixpanel"!==d&&(a+="."+d);b||(a+=" (stub)");return a};c.people.toString=function(){return c.toString(1)+".people (stub)"};i="disable track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.increment people.append people.track_charge people.clear_charges people.delete_user".split(" ");for(g=0;g<i.length;g++)f(c,i[g]);b._i.push([a,
    e,d])};b.__SV=1.2}})(document,window.mixpanel||[]);
    mixpanel.init("f71c19735fa6ecc5225ff563285e1794");
    </script>
<!-- Eloqua -->
<script type="text/javascript">
    var _elqQ = _elqQ || [];
    _elqQ.push(['elqSetSiteId', '815114181']);
    _elqQ.push(['elqTrackPageView']);
    _elqQ.push(['elqUseFirstPartyCookie', 'www.twilio.com']);

    (function () {
      function async_load() {
        var s = document.createElement('script'); s.type = 'text/javascript'; s.async = true;
        s.src = '//img03.en25.com/i/elqCfg.min.js';
        var x = document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(s, x);
      }
      if (window.addEventListener) window.addEventListener('DOMContentLoaded', async_load, false);
      else if (window.attachEvent) window.attachEvent('onload', async_load);
    })();
    </script>
<!-- Transifex -->
<script type="text/javascript">
    window.liveSettings = {
      api_key: '4c06c1c5a6b341e591d969476fe2675f'
    };
    </script>
<script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/live.js.download" type="text/javascript"></script>
<style>
    .txlive-langselector { display: none; }
    </style>
<script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/docs.min.722f741d2.js.download"></script>



    

    <!-- Initialize recaptcha v3 -->
<script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/api.js.download"></script>
<script type="application/javascript">window.reCAPTCHASiteKey = "6Ld1J2sUAAAAAEzfAkJKSWq8Za2Bt9Hw-rpCbBE9";</script>


    <!--  Initialize docsearch -->
    <script type="text/javascript" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/docsearch.min.js.download"></script>
    <script type="text/javascript"> docsearch({
     apiKey: window.twilio.DOCSEARCH_API_KEY,
     indexName: 'twilio',
     inputSelector: '#docsearch',
     debug: false, // Set debug to true if you want to inspect the dropdown
     algoliaOptions: {
         hitsPerPage: 6
     }
    });
    </script>
  

<iframe id="qualaroo_dnt_frame" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/frame.html" style="width: 1px; height: 1px; display: none; opacity: 0;"></iframe><script src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/adsct" type="text/javascript"></script><iframe name="_hjRemoteVarsFrame" title="_hjRemoteVarsFrame" id="_hjRemoteVarsFrame" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/box-5e3cec51ed8e99df6977c199d27812d7.html" style="display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; display: block; transition: right 0.3s ease 0s; position: fixed; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/anchor.html" width="256" height="60" role="presentation" name="a-hqe3rkbyn4ew" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./Twilio SMS Python Quickstart - Send &amp; Receive SMS - Twilio_files/saved_resource.html"></iframe></div></body></html>