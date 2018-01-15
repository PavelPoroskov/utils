
void StardictHeadwordsRequest::run()
{
  if ( Qt4x5::AtomicInt::loadAcquire( isCancelled ) )
  {
    finish();
    return;
  }

  try
  {
    vector< WordArticleLink > chain = dict.findArticles( word );

//( search alternatives for plural or for Past tense of regular verbs, 
//  useful when search with scan popup: 
//  only for Language_From==English and Format_Of_Dictionary=StarDict
//    (not in dictionary): books --> book (in dictionary),
//    (not in dictionary): classes --> class (in dictionary),
//    (not in dictionary): parties --> party (in dictionary),
//
//    (not in dictionary): worked --> work (in dictionary)
//    (not in dictionary): leveraged --> leverage (in dictionary)

    if ( (chain.size() == 0) && (dict.getLangFrom() == 28261) ) // "en"
    {
      wstring folded = Folding::apply( word );
      int lenWord = folded.size();

      // books --> book
      //if ( chain.size() == 0 )
      //{
      if ( 1 < lenWord && folded[lenWord - 1] == L's' )
      {
        wstring folded_noS = folded.substr( 0, lenWord - 1 );
        chain = dict.findArticles( folded_noS );

        // parties --> party
        if ( chain.size() == 0 )
        {
          if ( 3 < lenWord && folded.substr( lenWord - 3, 3 ) == L"ies" )
          {
            wstring folded_noIES = folded.substr( 0, lenWord - 3 ) + L"y";
            chain = dict.findArticles( folded_noIES );      
          }
        }

        // classes --> class
        if ( chain.size() == 0 )
        {
          if ( 2 < lenWord && folded.substr( lenWord - 2, 2 ) == L"es" )
          {
            wstring folded_noES = folded.substr( 0, lenWord - 2 );
            chain = dict.findArticles( folded_noES );      
          }
        }
      }
      //}


      // worked --> work
      if ( chain.size() == 0 )
      {
        if ( 2 < lenWord && folded.substr( lenWord - 2, 2 ) == L"ed" )
        {
          wstring folded_noED = folded.substr( 0, lenWord - 2 );
          chain = dict.findArticles( folded_noED );      
        }

        //leveraged --> leverage
        if ( chain.size() == 0 )
        {
          if ( 1 < lenWord && folded.substr( lenWord - 1, 1 ) == L"d" )
          {
            wstring folded_noD = folded.substr( 0, lenWord - 1 );
            chain = dict.findArticles( folded_noD );      
          }
        }
      }
    }
//)

    wstring caseFolded = Folding::applySimpleCaseOnly( word );

    for( unsigned x = 0; x < chain.size(); ++x )
    {
      if ( Qt4x5::AtomicInt::loadAcquire( isCancelled ) )
      {
        finish();
        return;
      }

      string headword, articleText;

      dict.loadArticle( chain[ x ].articleOffset,
                        headword, articleText );

      wstring headwordDecoded = Utf8::decode( headword );

      if ( caseFolded != Folding::applySimpleCaseOnly( headwordDecoded ) )
      {
        // The headword seems to differ from the input word, which makes the
        // input word its synonym.
        Mutex::Lock _( dataMutex );

        matches.push_back( headwordDecoded );
      }
    }
  }
  catch( std::exception & e )
  {
    setErrorString( QString::fromUtf8( e.what() ) );
  }

  finish();
}

