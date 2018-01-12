
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

//( search alternatives for plural, useful when search with scan popup: 
//  only for Language_From==English and Format_Of_Dictionary=StarDict
//    (not in dictionary): smokes --> smoke (in dictionary),
//    (not in dictionary): fishes --> fish (in dictionary),
//    (not in dictionary): fished --> fish (in dictionary)

    if ( (chain.size() == 0) && (dict.getLangFrom() == 28261) ) // "en"
    {
      wstring folded = Folding::apply( word );
      int lenWord = folded.size();

      // smokes --> smoke
      //if ( chain.size() == 0 )
      //{
      if ( 1 < lenWord && folded[lenWord - 1] == L's' )
      {
        wstring folded_noS = folded.substr( 0, lenWord - 1 );
        chain = dict.findArticles( folded_noS );      
      }
      //}

      // fishes --> fish
      if ( chain.size() == 0 )
      {
        if ( 2 < lenWord && folded.substr( lenWord - 2, 2 ) == L"es" )
        {
          wstring folded_noES = folded.substr( 0, lenWord - 2 );
          chain = dict.findArticles( folded_noES );      
        }
      }

      // fished --> fish
      if ( chain.size() == 0 )
      {
        if ( 2 < lenWord && folded.substr( lenWord - 2, 2 ) == L"ed" )
        {
          wstring folded_noED = folded.substr( 0, lenWord - 2 );
          chain = dict.findArticles( folded_noED );      
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

