#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ritex
Version  : 1.0.1
Release  : 4
URL      : https://rubygems.org/downloads/ritex-1.0.1.gem
Source0  : https://rubygems.org/downloads/ritex-1.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
Author::    William Morgan (mailto: wmorgan-ritex@masanjin.net)
License::   GNU GPL version 2

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ritex-1.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-ritex.gemspec

%build
gem build rubygem-ritex.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
ritex-1.0.1.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/ritex-1.0.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Error/cdesc-Error.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/LexError/cdesc-LexError.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Lexer/cdesc-Lexer.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Lexer/lex-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Lexer/lex_inner-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Lexer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Lexer/push-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/MathML/cdesc-MathML.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/MathML/generate-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/MathML/generate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/MathML/lookup-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/MathML/lookup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/MathML/markup-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/MathML/markup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/_reduce_none-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/cdesc-Parser.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/flush_macros-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/format%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/handle_mathml_markup-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/join-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/merror-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/op-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/parse-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/raw_funarg-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/safe-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/Parser/special-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/Ritex/cdesc-Ritex.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/String/map_chars-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/page-README.ri
/usr/lib64/ruby/gems/2.2.0/doc/ritex-1.0.1/ri/page-ReleaseNotes.ri
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/README
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/ReleaseNotes
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/lib/ritex.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/lib/ritex/lexer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/lib/ritex/mathml/entities.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/lib/ritex/mathml/functions.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/lib/ritex/mathml/markup.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/lib/ritex/parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/test/all.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/test/answer-key.yaml
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/test/mathml.rb
/usr/lib64/ruby/gems/2.2.0/gems/ritex-1.0.1/test/parser.rb
/usr/lib64/ruby/gems/2.2.0/specifications/ritex-1.0.1.gemspec
